"""add content to  posts table

Revision ID: 1c4b068f947e
Revises: f867eaf76e55
Create Date: 2025-04-10 12:10:43.595845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c4b068f947e'
down_revision: Union[str, None] = 'f867eaf76e55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
