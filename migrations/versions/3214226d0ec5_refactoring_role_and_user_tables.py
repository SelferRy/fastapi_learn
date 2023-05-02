"""Refactoring role and user tables

Revision ID: 3214226d0ec5
Revises: 7c9a38669d20
Create Date: 2023-05-02 22:59:15.270967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3214226d0ec5'
down_revision = '7c9a38669d20'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('roles', 'role')
    op.rename_table('users', 'user')


def downgrade() -> None:
    op.rename_table('role', 'roles')
    op.rename_table('user', 'users')
