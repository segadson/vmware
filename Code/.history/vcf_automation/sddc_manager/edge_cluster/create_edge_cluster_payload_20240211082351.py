from sddc_manager.clusters import clusters_functions

def create_edge_cluster_payload(sdd_manger_ip, vcf_token, domain_cluster_name):
    '''
    This function returns the payload for creating an edge cluster in SDDC Manager
    '''

    #Get Cluster ID for Edge Cluster Deployment
    clusters = clusters_functions.get_sddc_manager_clusters(sdd_manger_ip, vcf_token)
    for cluster in clusters['elements']:
        if cluster['name'] == domain_cluster_name:
            cluster_id = cluster['id']
            break
