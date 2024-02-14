import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

from sddc_manager.avns.avn_functions import create_avns, get_avn_id, create_avn_payload
from authentication.get_authentication_token import get_vcf_token
from sddc_manager.global_sddc_manager_functions import validate_sddc_manager_component_request, monitor_sddc_manager_validation
import json



# def create_sddc_manager_avns
# def main():
#     sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
#     domain_cluster_name = 'mgmt-cluster-01'
#     create_edge_cluster_on_domain(sddc_manager_ip, domain_cluster_name)

# if __name__ == "__main__":
#     main()