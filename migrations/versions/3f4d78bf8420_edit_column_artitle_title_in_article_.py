"""Edit column artitle_title  in Article Migration

Revision ID: 3f4d78bf8420
Revises: 5488bd12618c
Create Date: 2020-09-28 19:12:22.626868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4d78bf8420'
down_revision = '5488bd12618c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('article_title', sa.String(), nullable=True))
    op.drop_column('articles', 'artile_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('artile_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('articles', 'article_title')
    # ### end Alembic commands ###
