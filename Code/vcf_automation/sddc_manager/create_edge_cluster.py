import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

from edge_cluster.edge_cluster_functions import create_edge_cluster_payload, validate_edge_cluster, create_sddc_manager_edge_cluster
from authentication.get_authentication_token import get_vcf_token
from sddc_manager.global_sddc_manager_functions import validate_sddc_manager_component_request, monitor_sddc_manager_validation

print("This is my file to demonstrate best practices.")

def create_edge_cluster_on_domain(sddc_manager_ip, domain_cluster_name):
    # Get the VCF token
    vcf_token = get_vcf_token()

    payload = create_edge_cluster_payload(sddc_manager_ip, vcf_token, domain_cluster_name)
    # Call the SDDC Manager API to Validate the edge cluster
    #validate_edge_cluster(sddc_manager_ip, vcf_token, payload)

    # Call the SDDC Manager API to Create the edge cluster
    #create_sddc_manager_edge_cluster(sddc_manager_ip, vcf_token, payload)

    #return modified_data

def main():
    sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
    domain_cluster_name = 'mgmt-domain'
    create_edge_cluster_on_domain(sddc_manager_ip, domain_cluster_name)

if __name__ == "__main__":
    main()