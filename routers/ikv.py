from datetime import datetime, date
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session, session  # type: ignore
from sqlalchemy import select
import models
from models import IkvKenmDim, IkvIndDim, InkVerhVanBaanDm
from database import get_db
from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, Query
from fastapi.responses import Response
import schemas
from utils import is_valid_bsn
from typing import Annotated

router = APIRouter(prefix="/api/v0/ikv", tags=["Inkomstenverhoudingen (IKV)"])


@router.get("", status_code=status.HTTP_200_OK, response_model=List[
    schemas.InkVerhVanBaanDmSchema])
def get_posts(bsn: Annotated[str,Query(description="Burgerservicenummer (bsn), komma-gescheiden bij meerdere bsn's")],
#def get_posts(bsn: str = Query(...,description="Burgerservicenummer (bsn), komma-gescheiden bij meerdere bsn's"),
              begin_datum: str = "1900-01-01",
              eind_datum: str = "9999-01-01",
              db: Session = Depends(get_db)):

    bsn_lijst = [s.strip() for s in bsn.split(",")]
    bsn_geldig = [is_valid_bsn(bsn_nummer) for bsn_nummer in bsn_lijst ]
    if not all(bsn_geldig):
        raise HTTPException(status_code=400, detail="BSN invalid")

    try:
        begin_date: date = datetime.strptime(begin_datum, "%Y-%m-%d").date()
        eind_date: date = datetime.strptime(eind_datum, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM-DD")


    stmt = db.query(*(c for c in models.InkVerhVanBaanDm.__table__.columns
                  if
                  c.name not in ("ikv_indicatie", "ikv_kenmerk")),
                models.IkvKenmDim.cdaard,
                models.IkvKenmDim.srtiv).join(
    models.InkVerhVanBaanDm.kenmerk).filter(
    models.InkVerhVanBaanDm.bsn.in_(bsn_lijst),
    models.InkVerhVanBaanDm.jaarmaand_begindatum.between(begin_date,
                                                         eind_date)).order_by(
    InkVerhVanBaanDm.bsn.asc(),
    InkVerhVanBaanDm.jaarmaand_begindatum.asc())

    results = stmt.all()
    return results

