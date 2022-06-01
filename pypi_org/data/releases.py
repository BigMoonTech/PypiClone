import datetime
import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    major_version = sa.Column(sa.BigInteger, index=True)
    minor_version = sa.Column(sa.BigInteger, index=True)
    build_version = sa.Column(sa.BigInteger, index=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    comment = sa.Column(sa.String)
    url = sa.Column(sa.String)
    size = sa.Column(sa.BigInteger)

    @property
    def version_text(self):
        return f'{self.major_version}.{self.minor_version}.{self.build_version}'
