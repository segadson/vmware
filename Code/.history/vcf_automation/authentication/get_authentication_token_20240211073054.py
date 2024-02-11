import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_vcf_token():
    '''
    This function returns a VCF token for API authentication
    '''
    username = 'administrator@vsphere.local'
    password = 'VMware123!'
    sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
    url = f"https://{sddc_manager_ip}//v1/tokens"

    payload = json.dumps({
      "username": username,
      "password": password
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
      }
    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()['accessToken']


def get_vcenter_token():
    '''
    This function returns a vCenter token for API authentication
    '''
    username = 'administrator@vsphere.local'
    password = 'VMware123!'
    vcenter_ip = 'vcenter.vcf.sddc.lab'

    url = f"https://{vcenter_ip}/rest/com/vmware/cis/session"

    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
      }
    try:
        response = requests.post(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()['value']


def get_nsxt_token():
    '''
    This function returns a NSX-T token for API authentication
    '''
    username = 'admin'
    password = 'VMware123!'
    nsxt_ip = 'nsx-manager.vcf.sddc.lab'

    url = f"https://{nsxt_ip}/api/v1/login"

    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
      }
    try:
        response = requests.post(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()['token']