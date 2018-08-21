"""initial migration

Revision ID: b4ba0ece8d1a
Revises: 
Create Date: 2018-08-21 20:49:39.065734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4ba0ece8d1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('mobile', sa.String(length=11), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('pwd', sa.String(length=256), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.Column('image', sa.TEXT(), nullable=True),
    sa.Column('ac_type', sa.String(length=4), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('password_hash')
    )
    op.create_index(op.f('ix_users_addtime'), 'users', ['addtime'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_addtime'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###