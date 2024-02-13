from create_edge_cluster_payload import create_edge_cluster_payload
from edge_cluster_functions import validate_edge_cluster, create_edge_cluster
from authentication.get_authentication_token import get_vcf_token

print("This is my file to demonstrate best practices.")

def create_edge_cluster(sddc_manager_ip, domain_cluster_name):
    # Get the VCF token
    vcf_token = get_vcf_token()

    payload = create_edge_cluster_payload(sddc_manager_ip, vcf_token, domain_cluster_name)
    # Call the SDDC Manager API to Validate the edge cluster
    #validate_edge_cluster(sddc_manager_ip, vcf_token, payload)

    # Call the SDDC Manager API to Create the edge cluster
    #create_edge_cluster(sddc_manager_ip, vcf_token, payload)

    #return modified_data

def main():
    sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
    domain_cluster_name = 'mgmt-domain'
    create_edge_cluster(sddc_manager_ip, domain_cluster_name)

if __name__ == "__main__":
    main()