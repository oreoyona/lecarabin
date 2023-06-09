"""empty message

Revision ID: c5b6248f8892
Revises: 00f1e12a89de
Create Date: 2023-06-17 13:40:30.021709

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c5b6248f8892'
down_revision = '00f1e12a89de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', postgresql.ARRAY(sa.String(length=100)), nullable=True))
        batch_op.add_column(sa.Column('author', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('author')
        batch_op.drop_column('tag')

    # ### end Alembic commands ###
