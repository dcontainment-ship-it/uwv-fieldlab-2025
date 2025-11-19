from email.policy import default

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, true, text, ForeignKey, Date, Text  # type: ignore
from sqlalchemy.orm import relationship, Mapped, mapped_column  # type: ignore
from sqlalchemy.sql.expression import text  # type: ignore
from database import Base



class IkvKenmDim(Base):
    __tablename__ = "ikv_tikv_kenm_dim"

    ikv_kenm_key = Column(Integer, primary_key=True, nullable=False, comment="IKV kenmerk.")
    cdaard = Column(Integer, nullable=False, comment="Code aard arbeidsverhouding.")
    lbtab = Column(String(3), nullable=False, comment="Code loonbelastingtabel")
    srtiv = Column(String(2), nullable=False, comment="Code soort inkomstenverhouding.")

    # One-to-many: a kenmerk can appear in many inkomstenverhoudingen
    verh_baan = relationship("InkVerhVanBaanDm", back_populates="kenmerk")


class IkvIndDim(Base):
    __tablename__ = "ikv_tikv_ind_dim"

    ikv_ind_key = Column(Integer, primary_key=True, nullable=False, comment="IKV indicatie.")
    indarbovonbeptd = Column(String(255), nullable=False)
    indjrurennrm = Column(String(1), nullable=False)
    indoprov = Column(String(1), nullable=False)
    indpubaannonbeptd = Column(String(1), nullable=False)
    indschriftarbov = Column(String(1), nullable=False)
    indwao = Column(String(1), nullable=False)
    indww = Column(String(1), nullable=False)
    indzw = Column(String(1), nullable=False)

    # One-to-many: an indicatie can appear in many inkomstenverhoudingen
    verh_baan = relationship("InkVerhVanBaanDm", back_populates="indicatie")


class InkVerhVanBaanDm(Base):
    __tablename__ = "ikv_tink_verh_van_baan_dm"


    ikv_id = Column(Integer, primary_key=True,nullable=False, comment="Inkomsten verhouding nummer.")
    bsn = Column(String(9), nullable=False, comment="bsn")
    jaarmaand_begindatum = Column(Date, primary_key=True,comment="Begindatum maand inkomsten.")
    aantctrcturenpwk_mnd = Column(Integer, nullable=False, comment="Aantal contracturen per week.")
    aantverlu_mnd = Column(Integer, nullable=False, comment="Aantal verloonde uren per maand.")
    cao_kenmerk = Column(Integer, nullable=False, comment="CAO kenmerk.")
    ikv_indicatie = Column(Integer, ForeignKey("ikv_tikv_ind_dim.ikv_ind_key"), nullable=False)
    ctrctln_mnd = Column(Integer, nullable=False, comment="Contractloon per maand.")
    datum_begin_iko = Column(Date, nullable=False)
    datum_begin_ikv = Column(Date, nullable=False)
    datum_einde_iko = Column(Date, nullable=False)
    datum_einde_ikv = Column(Date, nullable=False)
    duur_iko = Column(Integer, nullable=False)
    gebdat_la = Column(Date, nullable=False)
    gesl_la = Column(String(5), nullable=False)
    ikv_kenmerk = Column(Integer, ForeignKey("ikv_tikv_kenm_dim.ikv_kenm_key"), nullable=False)
    lhnr = Column(String(255), nullable=False)
    lnlbph_mnd = Column(Integer, nullable=False)
    lnsv_mnd = Column(Integer, nullable=False)
    huidige_uren_per_week = Column(Integer, nullable=False, comment="Huidige contracturen per week.")
    gewerkte_weken_36 = Column(Integer, nullable=False, comment="Aantal gewerkte weken in de laatste 36 weken.")
    arbeidsverleden_jaren = Column(Text, nullable=False, comment="Jaren waarin arbeid is verricht (komma-gescheiden, b.v. '2005,2006,2017').")
    jaarloon_voorgaand_jaar = Column(Integer, nullable=False, comment="Bruto jaarloon in het voorgaande kalenderjaar.")
    heeft_wia = Column(String(1), nullable=False, comment="Indicatie of WIA: 'J' of 'N'.")
    heeft_ww = Column(String(1), nullable=False, comment="Indicatie of WW: 'J' of 'N'.")    
    # Relationships
    kenmerk = relationship("IkvKenmDim", back_populates="verh_baan")
    indicatie = relationship("IkvIndDim", back_populates="verh_baan")
