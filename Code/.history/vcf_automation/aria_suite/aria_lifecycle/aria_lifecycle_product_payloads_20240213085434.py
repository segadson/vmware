import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def create_workspace_one_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:
    -   fqdn: vRealize Suite Lifecycle Manager hostname
    -   nsxtStandaloneTier1Ip: Free IP address from the X-Region Application Virtual Network for the Standalone Tier 1 router
    -   sshPassword: vRealize Suite Lifecycle Manager root password
    -   apiPassword: vRealize Suite Lifecycle Manager API password
    '''
    payload = {}

    
    return payload