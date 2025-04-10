"""add foreign-key to posts table

Revision ID: 2da5bc3194db
Revises: 32e8b5acd083
Create Date: 2025-04-10 12:22:39.090389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2da5bc3194db'
down_revision: Union[str, None] = '32e8b5acd083'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk', 
        source_table='posts', 
        referent_table='users', 
        local_cols=['owner_id'], 
        remote_cols=['id'], 
        ondelete='CASCADE'
    )
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
