# All SQLAlchemy models placed here for model preloading.
# db_session.py can reference this one file, and eliminates
# the need to muck around in the global init.

# noinspection PyUnresolvedReferences
import pypi_org.data.audit
# noinspection PyUnresolvedReferences
import pypi_org.data.downloads
# noinspection PyUnresolvedReferences
import pypi_org.data.languages
# noinspection PyUnresolvedReferences
import pypi_org.data.licenses
# noinspection PyUnresolvedReferences
import pypi_org.data.maintainers
# noinspection PyUnresolvedReferences
import pypi_org.data.packages
# noinspection PyUnresolvedReferences
import pypi_org.data.releases
# noinspection PyUnresolvedReferences
import pypi_org.data.users
