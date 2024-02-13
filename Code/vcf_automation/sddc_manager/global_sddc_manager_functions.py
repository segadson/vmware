import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def validate_sddc_manager_component_request(sddc_manager_ip, vcf_token, validation_type, payload):
    '''
    This function validates a component in SDDC Manager
    Validation types:
    - sddc
    - workloadDomain
    - host
    - cluster
    - avn
    - storage
    - vcenter
    - nsx
    - edge-clusters
    '''
    url = f"https://{sddc_manager_ip}/v1/{validation_type}/validations"

    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    print(json.dumps(response.json(), indent=4))
    return response.json()

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
    
    print(json.dumps(response.json(), indent=4))
    return response.json()

def monitor_sddc_manager_validation(sddc_manager_ip, vcf_token, validation_type, request_id):
    '''
    This function monitors the status of a validation in SDDC Manager
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
    validation_status = get_sddc_manager_validation_status(sddc_manager_ip, vcf_token, validation_type, request_id)
    while validation_status['executionStatus'] == 'IN_PROGRESS':
        validation_status = get_sddc_manager_validation_status(sddc_manager_ip, vcf_token, validation_type, request_id)
    if validation_status['executionStatus'] == 'FAILED':
        raise SystemExit(f"Validation {request_id} failed with error: {validation_status['error']['message']}")
    return validation_status


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
    while task_status['executionStatus'] == 'IN_PROGRESS':
        task_status = get_sddc_manager_task_status(sddc_manager_ip, vcf_token, task_id)
    if task_status['executionStatus'] == 'FAILED':
        raise SystemExit(f"Task {task_id} failed with error: {task_status['error']['message']}")
    return task_status