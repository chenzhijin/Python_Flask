"""empty message

Revision ID: 98a7ab582a75
Revises: 
Create Date: 2017-10-16 11:35:23.564000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '98a7ab582a75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('content', mysql.TEXT(), nullable=False))
    # ### end Alembic commands ###
