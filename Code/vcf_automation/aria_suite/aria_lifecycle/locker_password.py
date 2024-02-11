import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

vrlcm_ip = 'vrlcm.vcf.sddc.lab'
username = 'admin'
password =  'VMware123!'

def get_vrlcm_locker_password(alias):
    '''
    This function returns the locker password for a given alias
    '''
    url = f"https://{vrlcm_ip}/lcm/locker/api/v2/passwords"

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

def create_vrlcm_locker_password(alias, username, password):
    '''
    This function creates a locker password for a given alias
    '''
    url = f"https://{vrlcm_ip}/lcm/locker/api/v2/passwords"

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
    