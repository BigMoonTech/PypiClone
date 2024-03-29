import sys
import os

# run the tests outside pycharm
container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)

# noinspection PyUnresolvedReferences
from account_tests import *
# noinspection PyUnresolvedReferences
from package_tests import *
# noinspection PyUnresolvedReferences
from home_tests import *
# noinspection PyUnresolvedReferences
from seo_tests import *
