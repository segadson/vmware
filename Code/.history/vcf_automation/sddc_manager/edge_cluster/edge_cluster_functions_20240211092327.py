import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from sddc_manager.edge_cluster import create_edge_cluster_payload

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
    return response.json()

def get_edge_cluster_id(sddc_manager_ip, vcf_token, edge_cluster_name):
    '''
    This function returns the id of an edge cluster in SDDC Manager
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
    return edge_cluster_id