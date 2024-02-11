import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_sddc_manager_clusters(sddc_manager_ip, vcf_token):
    '''
    This function returns the list of clusters in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/clusters"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()

def get_sddc_maanger_stretched_clusters(sddc_manager_ip, vcf_token):
    '''
    This function returns the list of stretched clusters in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/clusters?isStretched=true"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()