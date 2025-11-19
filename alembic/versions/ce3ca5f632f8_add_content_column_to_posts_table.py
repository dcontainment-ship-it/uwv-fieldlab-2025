"""Add content column to posts table

Revision ID: ce3ca5f632f8
Revises: d3b1df24c98b
Create Date: 2025-08-11 10:08:36.121656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ce3ca5f632f8'
down_revision: Union[str, Sequence[str], None] = 'd3b1df24c98b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(),
                                     nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
