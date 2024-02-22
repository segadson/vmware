import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from error_handling.return_json import return_json

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
    return payload

def deploy_aria_lifecycle(sddc_manager_ip, vcf_token, aria_lifecycle_payload):
    '''
    This function deploys Aria Lifecycle in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/vrslcms"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    response = requests.post(url, headers=headers, data=json.dumps(aria_lifecycle_payload), verify=False)
    request_json = response.json()
    try:
        response = requests.post(url, headers=headers, data=json.dumps(aria_lifecycle_payload), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()