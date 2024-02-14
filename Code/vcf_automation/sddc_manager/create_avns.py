import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

from sddc_manager.avns.avn_functions import create_avns, get_avn_id, create_avn_payload, validate_avn_creation
from authentication.get_authentication_token import get_vcf_token
from sddc_manager.global_sddc_manager_functions import validate_sddc_manager_component_request, monitor_sddc_manager_validation
import json



def create_sddc_manager_avns (sddc_manager_ip, edge_cluster_name):
    #Get VCF Token
    vcf_token = get_vcf_token()

    #Create AVN Payload
    payload = create_avn_payload(sddc_manager_ip, vcf_token, edge_cluster_name)

    #Validate AVN
    validate_avn_creation(sddc_manager_ip, vcf_token, payload)

    #Create AVN
    create_avns(sddc_manager_ip, vcf_token, payload)
    
def main():
    sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
    edge_cluster_name = 'EC-01'
    create_sddc_manager_avns(sddc_manager_ip, edge_cluster_name)

if __name__ == "__main__":
    main()