"""Add bool cols to user table

Revision ID: e7d6bcbdd27f
Revises: 3214226d0ec5
Create Date: 2023-05-02 23:23:00.288895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d6bcbdd27f'
down_revision = '3214226d0ec5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user', sa.Column('is_active', sa.Boolean, nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean, nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.Boolean, nullable=False))


def downgrade() -> None:
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_verified')
