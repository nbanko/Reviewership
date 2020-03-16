"""empty message

Revision ID: 67006cf3e056
Revises: 5c0fcba38c38
Create Date: 2020-03-11 11:56:11.229508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67006cf3e056'
down_revision = '5c0fcba38c38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('biling', sa.String(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('requestor', sa.String(), nullable=True),
    sa.Column('reviewer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###