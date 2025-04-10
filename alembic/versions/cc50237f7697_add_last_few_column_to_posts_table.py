"""add last few column to posts table

Revision ID: cc50237f7697
Revises: 2da5bc3194db
Create Date: 2025-04-10 12:27:34.022332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc50237f7697'
down_revision: Union[str, None] = '2da5bc3194db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade():
    op.drop_column('posts',  'published')
    op.drop_column('posts', 'created_at')
    pass
