"""hash add to user model

Revision ID: ff36e03a2f
Revises: 28f6cf810a3
Create Date: 2014-12-28 21:31:29.982068

"""

# revision identifiers, used by Alembic.
revision = 'ff36e03a2f'
down_revision = '28f6cf810a3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
