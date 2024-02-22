import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


from sddc_manager.edge_cluster.edge_cluster_functions import get_edge_cluster_id
from sddc_manager.global_sddc_manager_functions import validate_sddc_manager_component_request, monitor_sddc_manager_validation, monitor_sddc_manager_task
from error_handling.return_json import return_json

def create_avn_payload(sddc_manager_ip, vcf_token, edge_cluster_name, *args, **kwargs):
    '''
    This function creates the payload for AVN creation in SDDC Manager
    
    '''
    edge_cluster_id = get_edge_cluster_id(sddc_manager_ip, vcf_token, edge_cluster_name)

    payload = {
            "avns": [ {
                "gateway": "10.50.0.1",
                "mtu": 8940,
                "name": "region-seg01",
                "regionType": "REGION_A",
                "routerName": "VLC-Tier-1",
                "subnet": "10.50.0.0",
                "subnetMask": "255.255.255.0"
            }, {
                "gateway": "10.60.0.1",
                "mtu": 8940,
                "name": "xregion-seg01",
                "regionType": "X_REGION",
                "routerName": "VLC-Tier-1",
                "subnet": "10.60.0.0",
                "subnetMask": "255.255.255.0"
            }],
            "edgeClusterId": edge_cluster_id
        }
    
    return payload

def create_avns(sddc_manager_ip, vcf_token, avn_payload):
    '''
    This function creates AVNs in SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/avns"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    response = requests.post(url, headers=headers, data=json.dumps(avn_payload), verify=False)
    request_json = return_json(response)

    request_id = request_json['id']
    monitor_sddc_manager_task(sddc_manager_ip, vcf_token, request_id)

    #To Do: Add validation for AVN creation

    return request_json

def validate_avn_creation(sddc_manager_ip, vcf_token, avn_payload):
    '''
    This function validates the creation of AVNs in SDDC Manager
    '''
    response = validate_sddc_manager_component_request(sddc_manager_ip, vcf_token, "avns", avn_payload)
    request_id = response['id']
    resultStatus = response['resultStatus']
    executionStatus = response['executionStatus']

    if resultStatus == 'SUCCEEDED' and executionStatus == 'COMPLETED':
        print(f"AVN creation validation for {avn_payload['edgeClusterId']} completed successfully")
    else:
        raise SystemExit(f"AVN creation validation for {avn_payload['edgeClusterId']} failed")
    
def get_avn_id(sddc_manager_ip, vcf_token, avn_type, network_name):
    '''
    This function returns the id of an AVN in SDDC Manager
    by AVN type which can be:
    - REGION_A
    - X_REGION
    You also will need the network name to match the AVN
    '''
    url = f"https://{sddc_manager_ip}/v1/avns?regionType={avn_type}"
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
        if item['regionType'] == avn_type and item['name'] == network_name:
            avn = item

    if avn is None:
        raise SystemExit(f"AVN {avn_type} with name: not found in SDDC Manager")
    
    return avn