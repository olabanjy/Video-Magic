"""empty message

Revision ID: 95e7e83f096a
Revises: 
Create Date: 2019-04-25 19:00:43.589312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e7e83f096a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('thumbnail', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('short_desc', sa.String(length=500), nullable=True),
    sa.Column('vid', sa.String(length=500), nullable=False),
    sa.Column('post_date', sa.String(length=300), nullable=False),
    sa.Column('thumbnail', sa.String(length=500), nullable=False),
    sa.Column('cat_id', sa.Integer(), nullable=False),
    sa.Column('featured', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('categories')
    op.drop_table('admins')
    # ### end Alembic commands ###
