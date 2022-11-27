"""Init migration

Revision ID: 94dd291f1b78
Revises: 
Create Date: 2022-11-25 14:50:11.740771

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '94dd291f1b78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'books',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('book_uid', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=True),
        sa.Column('genre', sa.String(length=255), nullable=True),
        sa.Column('condition', sa.Enum('EXCELLENT', 'GOOD', 'BAD', name='condition'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.PrimaryKeyConstraint('book_uid'),
    )
    op.create_table(
        'library',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('library_uid', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('city', sa.String(length=255), nullable=False),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.PrimaryKeyConstraint('library_uid'),
    )
    op.create_table(
        'library_books',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('book_id', sa.Integer(), nullable=False),
        sa.Column('library_id', sa.Integer(), nullable=False),
        sa.Column('available_count', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['book_id'],
            ['books.id'],
        ),
        sa.ForeignKeyConstraint(
            ['library_id'],
            ['library.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library_books')
    op.drop_table('library')
    op.drop_table('books')
    # ### end Alembic commands ###
