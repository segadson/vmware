import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

aria_lifecycle_ip = 'vrlcm.vcf.sddc.lab'
username = 'admin'
password =  'VMware123!'

#########################################################
# Locker Functions
#########################################################

def get_vrlcm_locker_password(aria_lifecycle_ip,alias):
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

def create_vrlcm_locker_password(aria_lifecycle_ip,alias, username, password):
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
# Locker Datacenter Functions
#########################################################

def get_aria_life_cycle_datacenter(aria_lifecycle_ip,target_datacenter):
    '''
    This function returns the datacenter details for a given datacenter
    '''
    url = f"https://{aria_lifecycle_ip}/lcm/lcops/api/v2/{target_datacenter}"

    headers = { 'Content-Type': 'application/json', 'Accept': 'application/json' }

    try:
        response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    for item in response.json():
        if item['name'] == target_datacenter:
            datacenter =  item

    if datacenter == None:
        raise SystemExit(f"Datacenter {target_datacenter} not found")
    # datacenter['datacenterVmid']
    return datacenter

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

def get_aria_lifecycle_license_keys(arialifecycle_ip):
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