"""empty message

Revision ID: 19b3f9243f68
Revises: 476dacbdf758
Create Date: 2014-12-02 19:31:27.265140

"""

# revision identifiers, used by Alembic.
revision = '19b3f9243f68'
down_revision = '476dacbdf758'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('leader_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=12), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('team_user',
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img_file', sa.String(length=140), nullable=True),
    sa.Column('EXIF_LensSerialNumber', sa.String(length=140), nullable=True),
    sa.Column('MakerNote_SerialNumberFormat', sa.String(length=140), nullable=True),
    sa.Column('EXIF_BodySerialNumber', sa.String(length=140), nullable=True),
    sa.Column('MakerNote_InternalSerialNumber', sa.String(length=140), nullable=True),
    sa.Column('MakerNote_SerialNumber', sa.String(length=140), nullable=True),
    sa.Column('Image_BodySerialNumber', sa.String(length=140), nullable=True),
    sa.Column('Uploaded', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('app')
    op.drop_table('project_app')
    with op.batch_alter_table(u'crawl', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_model_id', sa.Integer(), nullable=True))

    with op.batch_alter_table(u'dashboard', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))

    with op.batch_alter_table(u'data_source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))

    with op.batch_alter_table(u'image_space', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))

    with op.batch_alter_table(u'plot', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'plot', schema=None) as batch_op:
        batch_op.drop_column('project_id')

    with op.batch_alter_table(u'image_space', schema=None) as batch_op:
        batch_op.drop_column('project_id')

    with op.batch_alter_table(u'data_source', schema=None) as batch_op:
        batch_op.drop_column('project_id')

    with op.batch_alter_table(u'dashboard', schema=None) as batch_op:
        batch_op.drop_column('project_id')

    with op.batch_alter_table(u'crawl', schema=None) as batch_op:
        batch_op.drop_column('data_model_id')

    op.create_table('project_app',
    sa.Column('project_id', sa.INTEGER(), nullable=True),
    sa.Column('app_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['app_id'], [u'app.id'], ),
    sa.ForeignKeyConstraint(['project_id'], [u'project.id'], )
    )
    op.create_table('app',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('icon', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('image')
    op.drop_table('team_user')
    op.drop_table('user')
    op.drop_table('team')
    op.drop_table('data_model')
    ### end Alembic commands ###