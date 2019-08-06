"""test

Revision ID: ef26cd0cfea8
Revises: f172a2ea80e8
Create Date: 2019-08-06 17:54:15.214994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef26cd0cfea8'
down_revision = 'f172a2ea80e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'age')
    # ### end Alembic commands ###
