"""Add last few columns to posts table

Revision ID: f44227c7a728
Revises: af0604b6820c
Create Date: 2025-08-11 12:15:55.026024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f44227c7a728'
down_revision: Union[str, Sequence[str], None] = 'af0604b6820c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False,
        server_default=sa.text('NOW()')), )


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
