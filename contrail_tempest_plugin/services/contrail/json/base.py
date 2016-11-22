from oslo_log import log as logging

from oslo_serialization import jsonutils as json

from tempest_lib import exceptions as lib_exc
from tempest_lib.common import rest_client

from six.moves.urllib import parse as urllib
import six

LOG = logging.getLogger(__name__)

class BaseContrailClient(rest_client.RestClient):
    """Base Tempest REST client for Contrail API"""