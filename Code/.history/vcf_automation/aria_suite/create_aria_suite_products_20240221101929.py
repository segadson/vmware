from aria_suite.aria_lifecycle import dummy_payload, aria_lifecycle_product_payloads



def create_edge_cluster_on_domain(sddc_manager_ip, domain_cluster_name):
    # Get the VCF token
    vcf_token = get_vcf_token()

    payload = create_edge_cluster_payload(sddc_manager_ip, vcf_token, domain_cluster_name)

    # Call the SDDC Manager API to Validate the edge cluster
    validate_edge_cluster(sddc_manager_ip, vcf_token, payload)

    # Call the SDDC Manager API to Create the edge cluster
    create_sddc_manager_edge_cluster(sddc_manager_ip, vcf_token, payload)

    #return modified_data

def main():
    sddc_manager_ip = 'sddc-manager.vcf.sddc.lab'
    domain_cluster_name = 'mgmt-cluster-01'
    create_edge_cluster_on_domain(sddc_manager_ip, domain_cluster_name)

if __name__ == "__main__":
    main()