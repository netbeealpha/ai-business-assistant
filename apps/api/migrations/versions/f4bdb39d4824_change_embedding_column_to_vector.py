"""change embedding column to vector

Revision ID: f4bdb39d4824
Revises: 1b667e381ca1
Create Date: 2026-09-01 23:50:00.674183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import pgvector.sqlalchemy
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f4bdb39d4824'
down_revision: Union[str, Sequence[str], None] = '1b667e381ca1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.execute(
        """
        ALTER TABLE knowledge_chunks
        ALTER COLUMN embedding TYPE VECTOR(384)
        USING NULL
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""

    op.execute(
        """
        ALTER TABLE knowledge_chunks
        ALTER COLUMN embedding TYPE JSON
        USING NULL
        """
    )
    # ### end Alembic commands ###
