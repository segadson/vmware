import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_sddc_manager_validation_status(sddc_manager_ip, vcf_token, validation_type, request_id):
    '''
    This function returns the validation status of SDDC Manager Component in VCF
    Validation types:
    - sddc
    - workloadDomain
    - host
    - cluster
    - avn
    - storage
    - vcenter
    - nsx
    - edge-cluster
    '''
    url = f"https://{sddc_manager_ip}/v1/{validation_type}/validations/{request_id}"
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

def get_sddc_manager_task_status(sddc_manager_ip, vcf_token, task_id):
    '''
    This function returns the status of a task in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/tasks/{task_id}"
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

def monitor_sddc_manager_task(sddc_manager_ip, vcf_token, task_id):
    '''
    This function monitors the status of a task in SDDC Manager
    '''
    task_status = get_sddc_manager_task_status(sddc_manager_ip, vcf_token, task_id)
    while task_status['status'] == 'IN_PROGRESS':
        task_status = get_sddc_manager_task_status(sddc_manager_ip, vcf_token, task_id)
    if task_status['status'] == 'FAILED':
        raise SystemExit(f"Task {task_id} failed with error: {task_status['error']['message']}")
    return task_status