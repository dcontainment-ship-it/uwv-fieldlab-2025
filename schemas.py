from datetime import datetime, date
from typing import Optional,Literal

from pydantic import BaseModel, EmailStr, ConfigDict, Field

class InkVerhVanBaanDmSchema(BaseModel):
    ikv_id: int = Field(...,description="IKV nummer")
    bsn: str = Field(...,description="burgerservicenummer: minimaal 1 bsn opgeven. Meerdere bsn's scheiden door een komma.")
    jaarmaand_begindatum: date = Field(...,description="Begindatum van de maand (werkelijke tijd), waarover gerapporteerd wordt.")
    aantctrcturenpwk_mnd: int = Field(...,description="Aantal contracturen per week. Het tussen de werkgever en werknemer vast overeengekomen aantal uren per week zoals opgenomen in of af te leiden uit de cao of individuele arbeidsovereenkomst of dat voortvloeit uit de publiekrechtelijke aanstelling of de fictieve dienstbetrekking.")
    aantverlu_mnd: int = Field(...,description="Aantal verloonde uren in een maand. Het aantal uren dat aan de werknemer voor de inkomstenverhouding in het aangiftetijdvak is verloond.")
    cao_kenmerk: int = Field(...,description="CAO kenmerk:  10129 = CAO Verpleeg-, Verzorgingshuizen, Thuiszorg en Jeugdgezondheidszorg \n 10105 = Bouw & Infra")
    ctrctln_mnd: int = Field(...,description="Contractloon. Het tussen de werkgever en werknemer vast overeengekomen bruto loon, zoals opgenomen in of af te leiden uit de cao of individuele arbeidsovereenkomst of dat voortvloeit uit de publiekrechtelijke aanstelling of de fictieve dienstbetrekking.")
    datum_begin_iko: date = Field(...,description="Begindatum van het tijdvak van de inkomstenopgave.")
    datum_begin_ikv: date = Field(...,description="Begindatum van de inkomstenverhouding.")
    datum_einde_iko: date = Field(...,description="Einddatum van het tijdvak van de inkomstenopgave.")
    datum_einde_ikv: date = Field(...,description="Einddatum van de inkomstenverhouding")
    duur_iko: int = Field(...,description="Lengte van het tijdvak inkomstenopgave in dagen.")
    gebdat_la: date = Field(...,description="Geboortedatum zoals opgegeven in de loonaangifte.")
    gesl_la: str = Field(...,description="Code die het geslacht van de natuurlijk persoon aangeeft, zoals opgegeven in de loonaangifte. 0 = Onbekend, 1 = Mannelijk, 2= Vrouwelijk, 9 = Niet gespecificeeerd")
    lhnr: str = Field(...,description="Loonheffingennummer. Een door de Belastingdienst toegekende identificatie waaronder de administratieve eenheid bekend is bij de UWV/Belastingdienst.")
    lnlbph_mnd: int = Field(...,description="Loon LB/PH. Het maand totaalbedrag waarover de loonbelasting/premie volksverzekeringen wordt berekend.")
    lnsv_mnd: int = Field(...,description="Loon SV. Het loon voor de werknemersverzekeringen.")
    cdaard: int = Field(...,description="Code aard arbeidsverhouding. Code die aangeeft welke soort arbeidsverhouding bepalend is voor de vaststelling dat de werknemer verplicht verzekerd is voor de werknemersverzekeringen.")
    srtiv: str = Field(...,description="Code soort inkomstenverhouding / inkomenscode. Code ter aanduiding van het soort inkomstenverhouding.")
    huidige_uren_per_week: int = Field(..., description="Huidige contracturen per week.")
    gewerkte_weken_36: int = Field(..., description="Aantal gewerkte weken in de afgelopen 36 weken.")
    arbeidsverleden_jaren: str = Field(..., description="Jaren waarin arbeid is verricht (komma-gescheiden, b.v. '2005,2006,2017').")     
    jaarloon_voorgaand_jaar: int = Field(..., description="Totaal bruto jaarloon in voorafgaand kalenderjaar.")
    heeft_wia: Literal["J", "N"] = Field(..., description="Indicatie of werknemer een WIA-uitkering heeft.")
    heeft_ww: Literal["J", "N"] = Field(..., description="Indicatie of werknemer een WW-uitkering heeft.")

    class Config:
        from_attributes = True




































