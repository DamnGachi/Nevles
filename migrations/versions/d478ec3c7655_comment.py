"""comment

Revision ID: d478ec3c7655
Revises: 75ce1a33ef44
Create Date: 2023-01-25 14:32:47.480531

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd478ec3c7655'
down_revision = '75ce1a33ef44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('nickname', sa.String(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('password', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_subscriber', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('nickname')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###