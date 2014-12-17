"""account confirmation

Revision ID: 3d5f56dbb689
Revises: e62be04a7e6
Create Date: 2014-12-16 22:40:06.830184

"""

# revision identifiers, used by Alembic.
revision = '3d5f56dbb689'
down_revision = 'e62be04a7e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
