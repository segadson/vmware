# tests/test_sddcmanagerwrapper.py

from pytest import fixture
from sddc_manager_wrapper import Domain

@fixture
def sddc_manager_domain_keys():
    # Responsible only for returning the test data

    return ['capacity','clusters','id','isManagementSsoDomain','name',
     'nsxtCluster','ssoId','ssoName','status','tags','type','vcenters']

def test_domain_info(sddc_manager_domain_keys):
    """Tests an API call to get a SDDC Manager Domain"""

    domain_instance = Domain("d2d6f866-b8ac-4d40-b20a-263046e7dd12")
    response = domain_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == "d2d6f866-b8ac-4d40-b20a-263046e7dd12", "The ID should be in the response"
    assert set(sddc_manager_domain_keys).issubset(response.keys()), "All keys should be in the response"