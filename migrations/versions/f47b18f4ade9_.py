"""empty message

Revision ID: f47b18f4ade9
Revises: 7476899a685c
Create Date: 2021-03-14 19:58:19.882438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47b18f4ade9'
down_revision = '7476899a685c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('complete', sa.Boolean(), nullable=True))
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('todos', 'complete')
    # ### end Alembic commands ###
