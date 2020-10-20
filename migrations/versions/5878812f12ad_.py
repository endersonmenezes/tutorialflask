"""empty message

Revision ID: 5878812f12ad
Revises: 
Create Date: 2020-10-20 19:19:13.472744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5878812f12ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teste_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teste_db_email'), 'teste_db', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teste_db_email'), table_name='teste_db')
    op.drop_table('teste_db')
    # ### end Alembic commands ###
