"""empty message

Revision ID: 580954f26379
Revises: 971da8bf49cd
Create Date: 2019-11-28 15:22:44.568434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '580954f26379'
down_revision = '971da8bf49cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('write_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
