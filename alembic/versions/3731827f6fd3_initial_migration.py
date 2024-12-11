"""Initial migration

Revision ID: 3731827f6fd3
Revises: 8bb87dd0fcdc
Create Date: 2024-12-11 17:06:04.592517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3731827f6fd3'
down_revision: Union[str, None] = '8bb87dd0fcdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_test_id', table_name='test')
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_pkey')
    )
    op.create_index('ix_test_id', 'test', ['id'], unique=False)
    # ### end Alembic commands ###