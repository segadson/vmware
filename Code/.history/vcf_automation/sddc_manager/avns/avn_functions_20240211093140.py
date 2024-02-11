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

