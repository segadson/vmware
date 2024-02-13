import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from sddc_manager.edge_cluster import create_edge_cluster_payload
from sddc_manager.global_sddc_manager_functions import validate_sddc_manager_component_request, monitor_sddc_manager_validation
from sddc_manager.global_sddc_manager_functions import monitor_sddc_manager_task

def validate_edge_cluster(sddc_manager_ip, vcf_token, edge_cluster_payload):
    '''
    This function validates an edge cluster in SDDC Manager
    '''
    validation_type = 'edge-clusters'
    response = validate_sddc_manager_component_request(sddc_manager_ip, vcf_token, validation_type, edge_cluster_payload)
    request_id = response['requestId']
    monitor_sddc_manager_validation(sddc_manager_ip, vcf_token, validation_type, request_id)

def create_sddc_manager_edge_cluster(sddc_manager_ip, vcf_token, edge_cluster_payload):
    '''
    This function creates an edge cluster in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/edge-clusters"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(edge_cluster_payload), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    request_id = response.json()['requestId']
    monitor_sddc_manager_task(sddc_manager_ip, vcf_token, request_id)

def get_edge_cluster_id(sddc_manager_ip, vcf_token, edge_cluster_name):
    '''
    This function returns the id of an edge cluster in SDDC Manager
    by edge cluster name
    '''
    url = f"https://{sddc_manager_ip}/v1/edge-clusters"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    for item in response.json():
        if item['name'] == edge_cluster_name:
            edge_cluster_id = item['id']

    if edge_cluster_id is None:
        raise SystemExit(f"Edge Cluster {edge_cluster_name} not found in SDDC Manager")
    
    return edge_cluster_id