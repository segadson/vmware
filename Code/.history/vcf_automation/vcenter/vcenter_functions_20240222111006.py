import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from authentication import get_authentication_token

vcenter_ip = 'vcenter.vcf.sddc.lab'

def get_vcenter_resource_pool(vcenter_ip, vcf_token, vcenter_name, resource_pool_name):
    '''
    This function returns the id of a resource pool in vCenter
    by vCenter name and resource pool name
    '''
    vcenter_token = get_authentication_token.get_vcenter_token()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'vmware-api-session-id': vcenter_token 
    }

    url = f"https://{vcenter_ip}/rest/vcenter/resource-pool"

    response = requests.get(url, headers=headers, verify=False)
    request_json = response.json()

    for item in request_json['value']:
        if item['name'] == 'Resources':
            resource_pool_id = item['resource_pool']

    if resource_pool_id is None:
        raise SystemExit(f"Resource pool {resource_pool_name} not found in vCenter {vcenter_name}")
    
    return f"{resource_pool_id}(Resources)"

def get_vcenter_vsan_storages(vcenter_ip):
    '''
    This function returns the id of a vsan storage in vCenter
    by vCenter name and vsan storage name
    '''
    vcenter_token = get_authentication_token.get_vcenter_token()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'vmware-api-session-id': vcenter_token 
    }

    url = f"https://{vcenter_ip}/rest/vcenter/datastore?filter.types=vsan"

    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()[0]['name']