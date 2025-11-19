"""Create posts table

Revision ID: d3b1df24c98b
Revises: 
Create Date: 2025-08-11 09:51:38.948464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd3b1df24c98b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts', sa.Column('id',
                                       sa.Integer(), nullable=False,
                                       primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
