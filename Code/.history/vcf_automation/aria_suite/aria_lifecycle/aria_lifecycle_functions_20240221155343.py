import requests
import json
import time
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

aria_lifecycle_ip = 'aria_lifecycle.vcf.sddc.lab'
username = 'admin'
password =  'VMware123!'

def return_json(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    # Must have been a 200 status code
    json_obj = response.json()
    return json_obj

#########################################################
# Locker Functions
#########################################################

def get_aria_lifecycle_locker_password(aria_lifecycle_ip,alias):
    '''
    This function returns the locker password for a given alias
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/passwords"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json():
        if item['alias'] == alias:
            password_alias =  item['password']

    if password_alias == None:
        raise SystemExit(f"Alias {alias} not found")
    
    return password_alias

def create_aria_lifecycle_locker_password(aria_lifecycle_ip,alias, username, password):
    '''
    This function creates a locker password for a given alias
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/passwords"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps({
    "alias": alias,
    "password": password,
    "passwordDescription": f"This password is being used for {alias}",
    "userName": username
    })

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

#########################################################
# Datacenter Functions
#########################################################

def get_aria_life_cycle_datacenter(aria_lifecycle_ip,target_datacenter):
    '''
    This function returns the datacenter details for a given datacenter
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/{target_datacenter}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    # try:
    #     response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    # except requests.exceptions.RequestException as e:
    #     raise SystemExit(e)
    # print(response)

    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    return_json(response)

    for item in response.json():
        if item['dataCenterName'] == target_datacenter:
            datacenter =  item

    if datacenter == None:
        raise SystemExit(f"Datacenter {target_datacenter} not found")
    # datacenter['datacenterVmid']
    return datacenter

def get_aria_lifecycle_datacenter_vcenter(aria_lifecycle_ip, target_datacenter, target_vcenter):
    '''
    This function returns the vCenter details for a given vCenter
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/datacenters/{target_datacenter}/vcenters{target_vcenter}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json():
        if item['vCenterName'] == target_vcenter:
            vcenter =  item

    if vcenter == None:
        raise SystemExit(f"vCenter {target_vcenter} not found")
    
    return vcenter

def get_aria_lifecycle_vcenter(aria_lifecycle_ip, target_datacenter, target_vcenter):
    '''
    This function returns the vCenter details for a given vCenter
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/datacenters/{target_datacenter}/vcenters{target_vcenter}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json():
        if item['name'] == target_vcenter:
            vcenter =  item

    if vcenter == None:
        raise SystemExit(f"vCenter {target_vcenter} not found")
    
    return vcenter

def get_aria_lifecycle_dns(aria_lifecycle_ip):
    '''
    This function returns the DNS details for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/settings/dns"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    if response.json() == None:
        raise SystemExit(f"No DNS found")
    
    return response.json()

def get_aria_lifecycle_ntp(aria_lifecycle_ip):
    '''
    This function returns the NTP details for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/settings/ntp-servers"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    if response.json() == None:
        raise SystemExit(f"No NTP found")
    
    return response.json()

def get_aria_lifecycle_license_keys(aria_lifecycle_ip):
    '''
    This function returns the license keys for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/active/licenses"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    if response.json() == None:
        raise SystemExit(f"No license keys found")
    
    return response.json()

def get_aria_lifecycle_license_keys_by_alias(aria_lifecycle_ip,license_key_alias):
    '''
    This function returns the license keys for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/licenses/alias/{license_key_alias}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_environment(aria_lifecycle_ip):
    '''
    This function returns the environment details for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/environments"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    if response.json() == None:
        raise SystemExit(f"No environment found")
    
    return response.json()

#########################################################
# Create License Keys
#########################################################
def create_aria_lifecycle_license_keys(aria_lifecycle_ip,license_key_alias, license_key):
    '''
    This function creates a license key for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/license/validate-and-add"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps({
    "alias": license_key_alias,
    "serialKey": license_key,
    "tenant": ""
    })

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_license_keys_by_alias(aria_lifecycle_ip,license_key_alias):
    '''
    This function returns the license keys for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/licenses/alias/{license_key_alias}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json():
        if item['alias'] == license_key_alias:
            license_key =  item

    if license_key == None:
        raise SystemExit(f"License Key {license_key_alias} not found")
    
    return license_key
#########################################################
# Create Certificates
# Get Certificates
#########################################################

def create_aria_lifecycle_certificate(aria_lifecycle_ip,alias, hostnames, ip_addresses):
    '''
    This function creates a certificate for Aria Lifecycle
    Need a List of Hostnames and a List of IP Addresses
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/certificates"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps({
            "alias": alias,
            "c": "IN",
            "cN": "cert1",
            "host": [
                hostnames
            ],
            "ip": [
                ip_addresses
            ],
            "l": "IN",
            "o": "vmware",
            "oU": "vmware",
            "sT": "IN",
            "size": 2048,
            "tenant": "string",
            "validity": 729
            })

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def import_aria_lifecycle_certificate(aria_lifecycle_ip,alias, certificat_chain, passphrase, private_key):
    '''
    This function imports a certificate for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/certificates/import"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps({
    "certificateChain": certificat_chain,
    "privateKey": private_key,
    "passphrase": passphrase
    })

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_certificate(aria_lifecycle_ip,alias):
    '''
    This function returns the certificate for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/locker/api/v2/certificates/"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json()['certificates']:
        if item['alias'] == alias:
            certificate =  item

    if certificate == None:
        raise SystemExit(f"Certificate {alias} not found")
    
    return certificate

def prevalidate_aria_lifecycle_enviornment(aria_lifecycle_ip,payload):
    '''
    This function prevalidates the environment for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/environments/pre-validate"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps(payload)

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def create_aria_lifecycle_environment(aria_lifecycle_ip,payload):
    '''
    This function creates the environment for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/environments"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    payload = json.dumps(payload)

    try:
        response = requests.post(url, headers=headers, data=payload, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_request_status(aria_lifecycle_ip, request_id):
    '''
    This function returns the request status for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/requests/{request_id}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_request_details(aria_lifecycle_ip, request_id):
    '''
    This function returns the request details for Aria Lifecycle Request
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/requests/{request_id}/requestDetails"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def get_aria_lifecycle_request_errors(aria_lifecycle_ip, request_id):
    '''
    This function returns the request errors for Aria Lifecycle Request
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/requests/{request_id}/error-causes"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def retry_aria_lifecycle_request(aria_lifecycle_ip, request_id):
    '''
    This function retries the request for Aria Lifecycle
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/requests/{request_id}/retry"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.post(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return response.json()

def monitor_aria_lifecycle_request(aria_lifecycle_ip, request_id):
    '''
    This function monitors the request for Aria Lifecycle
    '''
    task_status = get_aria_lifecycle_request_status(aria_lifecycle_ip, request_id)
    while task_status['status'] == 'IN_PROGRESS':
        task_status = get_aria_lifecycle_request_status(aria_lifecycle_ip, request_id)
        print(json.dumps(task_status, indent=4))
        time.sleep(15)
    if task_status['status'] == 'FAILED':
        request_error = get_aria_lifecycle_request_errors(aria_lifecycle_ip, request_id)
        raise SystemExit(f"Request {request_id} failed with error: {request_error['errorCode']: request_error['message']}")