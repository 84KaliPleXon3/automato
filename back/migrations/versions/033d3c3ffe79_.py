"""empty message

Revision ID: 033d3c3ffe79
Revises: b04011c66f30
Create Date: 2020-01-07 18:28:41.146110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '033d3c3ffe79'
down_revision = 'b04011c66f30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('meta', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'meta')
    # ### end Alembic commands ###
