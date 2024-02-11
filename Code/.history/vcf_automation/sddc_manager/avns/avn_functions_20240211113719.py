import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


from sddc_manager.edge_cluster import get_edge_cluster_id

def create_avn_payload(edge_cluster_name, *args, **kwargs):
    '''
    This function creates the payload for AVN creation in SDDC Manager
    
    '''
    edge_cluster_id = get_edge_cluster_id(edge_cluster_name)

    payload = {
        "edgeClusterId" : edge_cluster_id,
        "avns" : [ {
            "name" : "sfo-m01-seg01",
            "regionType" : "REGION_A",
            "subnet" : "192.168.20.0",
            "subnetMask" : "255.255.255.0",
            "gateway" : "192.168.20.1",
            "mtu" : 9000,
            "routerName" : "sfo-m01-seg01-t0-gw01"
        }, {
            "name" : "xreg-m01-seg01",
            "regionType" : "X_REGION",
            "subnet" : "192.168.30.0",
            "subnetMask" : "255.255.255.0",
            "gateway" : "192.168.30.1",
            "mtu" : 9000,
            "routerName" : "xreg-m01-seg01-t0-gw01"
        } ]
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
    try:
        response = requests.post(url, headers=headers, data=json.dumps(avn_payload), verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()

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