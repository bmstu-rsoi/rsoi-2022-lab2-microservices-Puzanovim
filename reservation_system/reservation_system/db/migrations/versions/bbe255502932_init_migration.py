"""Init migration

Revision ID: bbe255502932
Revises: 
Create Date: 2022-11-26 17:52:12.350357

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bbe255502932'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'reservation',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('reservation_uid', postgresql.UUID(as_uuid=True), unique=True, nullable=True),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('book_uid', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('library_uid', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', sa.Enum('RENTED', 'RETURNED', 'EXPIRED', name='status'), nullable=False),
        sa.Column('start_date', postgresql.TIMESTAMP(), nullable=False),
        sa.Column('till_date', postgresql.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
