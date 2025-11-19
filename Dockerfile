FROM python:3.13.7-slim

RUN mkdir -p /var/log/my_app
RUN chown -R www-data:www-data /var/log/my_app

ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV UVICORN_CMD_ARGS="--proxy-headers"
#Gunicorn passes UVICORN_CMD_ARGS to each Uvicorn worker it spawns.

CMD ["gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]




