"""empty message

Revision ID: 6bbf570c7861
Revises: 
Create Date: 2020-09-23 16:11:19.986926

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6bbf570c7861'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_completo', sa.String(length=255), nullable=True),
    sa.Column('cpf', sa.String(length=14), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('data_cadastro', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('batidas__ponto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('tipo_batida', sa.String(length=14), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('batidas__ponto')
    op.drop_table('usuario')
    # ### end Alembic commands ###
