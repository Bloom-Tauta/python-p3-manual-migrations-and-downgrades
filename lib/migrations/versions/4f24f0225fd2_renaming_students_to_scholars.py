"""Renaming students to scholars

Revision ID: 4f24f0225fd2
Revises: 791279dd0760
Create Date: 2024-08-26 18:04:46.753753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f24f0225fd2'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
