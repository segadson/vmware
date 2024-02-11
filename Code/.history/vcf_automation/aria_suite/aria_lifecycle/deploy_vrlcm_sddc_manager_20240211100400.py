'''
- AVNs
- Unique vRealize Suite Lifecycle Manager hostname and corresponding IP address from the X-Region Application Virtual Network
- vRealize Suite Lifecycle Manager API and root passwords
- vRealize Suite Lifecycle Manager certificate
- Free IP address from the X-Region Application Virtual Network for the Standalone Tier 1 router
- he vRealize Suite Lifecycle Manager bundle needs to be downloaded and applied on the SDDC Manager
- Application Virtual Network should have connectivity to the management VLAN
'''
import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def create_aria_lifecycle_payload(*args, **kwargs):
    '''
    This function creates the payload for Aria Lifecycle deployment in SDDC Manager
    Arguments:
    -   fqdn: vRealize Suite Lifecycle Manager hostname
    -   nsxtStandaloneTier1Ip: Free IP address from the X-Region Application Virtual Network for the Standalone Tier 1 router
    -   sshPassword: vRealize Suite Lifecycle Manager root password
    -   apiPassword: vRealize Suite Lifecycle Manager API password
    '''
    payload = {
            "apiPassword": "string",
            "fqdn": "vrslcm.vrack.vsphere.local",
            "nsxtStandaloneTier1Ip": "string",
            "sshPassword": "string"
        }
    