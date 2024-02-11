import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_vcf_token():
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