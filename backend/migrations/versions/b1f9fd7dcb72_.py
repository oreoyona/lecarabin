"""empty message

Revision ID: b1f9fd7dcb72
Revises: c5b6248f8892
Create Date: 2023-06-17 13:47:00.957802

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b1f9fd7dcb72'
down_revision = 'c5b6248f8892'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', postgresql.ARRAY(sa.String(length=100)), nullable=True))
        batch_op.add_column(sa.Column('author', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('author')
        batch_op.drop_column('tag')

    # ### end Alembic commands ###