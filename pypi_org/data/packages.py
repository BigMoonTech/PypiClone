import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypi_org.data.modelbase import SqlAlchemyBase
from pypi_org.data.releases import Release


class Package(SqlAlchemyBase):
    """Declaration for the package model."""

    # sqlAlchemy would name table 'Package', so rename it 'packages'
    __tablename__ = 'packages'

    # all the column names:
    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    # add a new column to test alembic
    last_updated = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    # relationship to releases:
    releases = orm.relationship(
        'Release',
        order_by=[
            Release.major_version.desc(),
            Release.minor_version.desc(),
            Release.build_version.desc()
        ],
        back_populates='package'
    )

    def __repr__(self):
        return f'<Package {self.id}>'
