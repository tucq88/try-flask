"""create posts table

Revision ID: 321f6007986c
Revises:
Create Date: 2019-03-07 09:31:17.938247+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '321f6007986c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('content', sa.Text()),
        sa.Column('created_at', sa.DateTime(
            timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(
            timezone=True), server_default=sa.func.now(), onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('posts')
