"""empty message

Revision ID: 48f679624cf3
Revises: fe2184926536
Create Date: 2016-05-31 13:53:42.621359

"""

# revision identifiers, used by Alembic.
revision = '48f679624cf3'
down_revision = 'fe2184926536'

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table('daily_reading'):
        op.add_column('daily_reading', sa.Column('user_id', sa.Integer(), nullable=True))
        op.create_foreign_key(None, 'daily_reading', 'user', ['user_id'], ['id'])
        op.drop_column('user', 'is_active')

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), nullable=True))
    op.drop_constraint(None, 'daily_reading', type_='foreignkey')
    op.drop_column('daily_reading', 'user_id')
    ### end Alembic commands ###
