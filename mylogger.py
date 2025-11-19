import logging
import json
import traceback
from datetime import datetime


class MyJSONFormatter(logging.Formatter):
    """
    Custom JSON log formatter for FastAPI/Gunicorn/Uvicorn.
    Produces ISO8601 timestamps and includes exception info.
    """

    def __init__(self, fmt_keys=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Default mapping of JSON keys → LogRecord attributes
        self.fmt_keys = fmt_keys or {
            "time": "asctime",
            "level": "levelname",
            "message": "message",
            "logger": "name",
            "module": "module",
            "function": "funcName",
            "line": "lineno",
            "process": "process",
            "thread": "threadName",
        }

    def formatTime(self, record, datefmt=None):
        # ISO8601 with timezone (UTC if not provided)
        return datetime.fromtimestamp(record.created).isoformat()

    def formatException(self, ei):
        return "".join(traceback.format_exception(*ei))

    def format(self, record):
        log_record = {}

        # Ensure asctime is set
        record.asctime = self.formatTime(record)

        for key, attr in self.fmt_keys.items():
            value = getattr(record, attr, None)
            if callable(value):  # avoid functions
                try:
                    value = value()
                except Exception:
                    value = str(value)
            log_record[key] = value

        # Handle exceptions (stack traces)
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        # Handle extra fields (FastAPI, uvicorn adds extra like "status", "method")
        if hasattr(record, "__dict__"):
            for k, v in record.__dict__.items():
                if k not in log_record and not k.startswith("_"):
                    try:
                        json.dumps(v)  # only include JSON serializable
                        log_record[k] = v
                    except (TypeError, ValueError):
                        log_record[k] = str(v)

        return json.dumps(log_record, ensure_ascii=False)
