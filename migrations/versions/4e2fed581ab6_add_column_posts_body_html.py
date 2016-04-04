"""add column:posts.body_html

Revision ID: 4e2fed581ab6
Revises: db99188b8724
Create Date: 2016-04-02 07:07:01.385000

"""

# revision identifiers, used by Alembic.
revision = '4e2fed581ab6'
down_revision = 'db99188b8724'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###