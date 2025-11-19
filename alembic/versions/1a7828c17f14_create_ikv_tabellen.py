"""Create IKV tabellen

Revision ID: 1a7828c17f14
Revises: 5435030c1a4e
Create Date: 2025-08-25 12:23:04.819917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a7828c17f14'
down_revision: Union[str, Sequence[str], None] = '5435030c1a4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ikv_tikv_kenm_dim',
        sa.Column('ikv_kenm_key', sa.Integer(), primary_key=True, nullable=False,
                  comment="IKV kenmerk."),
        sa.Column('cdaard', sa.Numeric(10, 0), nullable=False,
                  comment="Code aard arbeidsverhouding."),
        sa.Column('lbtab', sa.String(3), nullable=False,
                  comment="Code loonbelastingtabel"),
        sa.Column('srtiv', sa.String(2), nullable=False,
                  comment="Code soort inkomstenverhouding.")
    )

    op.create_table(
        'ikv_tikv_ind_dim',
        sa.Column('ikv_ind_key', sa.Integer(), primary_key=True, nullable=False,
                  comment="IKV indicatie."),
        sa.Column('indarbovonbeptd', sa.String(255), nullable=False),
        sa.Column('indjrurennrm', sa.String(1), nullable=False),
        sa.Column('indoprov', sa.String(1), nullable=False),
        sa.Column('indpubaannonbeptd', sa.String(1), nullable=False),
        sa.Column('indschriftarbov', sa.String(1), nullable=False),
        sa.Column('indwao', sa.String(1), nullable=False),
        sa.Column('indww', sa.String(1), nullable=False),
        sa.Column('indzw', sa.String(1), nullable=False)
    )

    """Upgrade schema by adding FK relations."""
    op.create_table(
        'ikv_tink_verh_van_baan_dm',
        sa.Column('ikv_id', sa.Integer(),  nullable=False,
                  comment="Inkomsten verhouding nummer."),
        sa.Column('bsn', sa.String(), nullable=False,
                  comment="Burgerservicenummer."),
        sa.Column('jaarmaand_begindatum', sa.Date(), nullable=False,
                  comment="Begindatum maand inkomsten."),
        sa.Column('aantctrcturenpwk_mnd', sa.Integer(), nullable=False,
                  comment="Aantal contracturen per week."),
        sa.Column('aantverlu_mnd', sa.Integer(), nullable=False,
                  comment="Aantal verloonde uren per maand."),
        sa.Column('cao_kenmerk', sa.Integer(), nullable=False,
                  comment="CAO kenmerk."),
        sa.Column('ikv_indicatie', sa.Integer(),
                  sa.ForeignKey('ikv_tikv_ind_dim.ikv_ind_key', ondelete="CASCADE"),
                  nullable=False,
                  comment="IKV indicatie."),
        sa.Column('ctrctln_mnd', sa.Integer(), nullable=False,
                  comment="Contractloon per maand."),
        sa.Column('datum_begin_iko', sa.Date(), nullable=False),
        sa.Column('datum_begin_ikv', sa.Date(), nullable=False),
        sa.Column('datum_einde_iko', sa.Date(), nullable=False),
        sa.Column('datum_einde_ikv', sa.Date(), nullable=False),
        sa.Column('duur_iko', sa.Integer(), nullable=False),
        sa.Column('gebdat_la', sa.Date(), nullable=False),
        sa.Column('gesl_la', sa.String(5), nullable=False),
        sa.Column('ikv_kenmerk', sa.Integer(),
                  sa.ForeignKey('ikv_tikv_kenm_dim.ikv_kenm_key', ondelete="CASCADE"),
                  nullable=False,
                  comment="IKV kenmerk."),
        sa.Column('lhnr', sa.String(255), nullable=False),
        sa.Column('lnlbph_mnd', sa.Integer(), nullable=False),
        sa.Column('lnsv_mnd', sa.Integer(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema by removing FK relations and tables."""
    op.drop_table('ikv_tikv_kenm_dim')
    op.drop_table('ikv_tikv_ind_dim')
    op.drop_table('ikv_tink_verh_van_baan_dm')
