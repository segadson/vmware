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

    if cluster_id is None:
        raise SystemExit(f"Cluster {domain_cluster_name} not found in SDDC Manager")
    
    payload = {
                "edgeClusterName":"WLD01-EC01",
                "edgeClusterType":"NSX-T",
                "edgeRootPassword":"VMware1!VMware1!",
                "edgeAdminPassword":"VMware1!VMware1!",
                "edgeAuditPassword":"VMware1!VMware1!",
                "edgeFormFactor":"MEDIUM",
                "tier0ServicesHighAvailability":"ACTIVE_ACTIVE",
                "mtu":9000,
                "asn":65005,
                "edgeNodeSpecs":[
                    {
                        "edgeNodeName":"wld-edge01.vstellar.local",
                        "managementIP":"172.16.10.115/24",
                        "managementGateway":"172.16.10.1",
                        "edgeTepGateway":"172.16.70.1",
                        "edgeTep1IP":"172.16.70.11/24",
                        "edgeTep2IP":"172.16.70.12/24",
                        "edgeTepVlan":700,
                        "clusterId":cluster_id,
                        "interRackCluster":False,
                        "uplinkNetwork":[
                            {
                            "uplinkVlan":500,
                            "uplinkInterfaceIP":"172.16.50.10/24",
                            "peerIP":"172.16.50.1/24",
                            "asnPeer":65001,
                            "bgpPeerPassword":"VMware1!"
                            },
                            {
                            "uplinkVlan":600,
                            "uplinkInterfaceIP":"172.16.60.10/24",
                            "peerIP":"172.16.60.1/24",
                            "asnPeer":65001,
                            "bgpPeerPassword":"VMware1!"
                            }
                        ]
                    },
                    {
                        "edgeNodeName":"wld-edge02.vstellar.local",
                        "managementIP":"172.16.10.116/24",
                        "managementGateway":"172.16.10.1",
                        "edgeTepGateway":"172.16.70.1",
                        "edgeTep1IP":"172.16.70.13/24",
                        "edgeTep2IP":"172.16.70.14/24",
                        "edgeTepVlan":700,
                        "clusterId":"81bc0275-1a09-455d-91fd-3fce591cf500",
                        "interRackCluster":False,
                        "uplinkNetwork":[
                            {
                            "uplinkVlan":500,
                            "uplinkInterfaceIP":"172.16.50.11/24",
                            "peerIP":"172.16.50.1/24",
                            "asnPeer":65001,
                            "bgpPeerPassword":"VMware1!"
                            },
                            {
                            "uplinkVlan":600,
                            "uplinkInterfaceIP":"172.16.60.11/24",
                            "peerIP":"172.16.60.1/24",
                            "asnPeer":65001,
                            "bgpPeerPassword":"VMware1!"
                            }
                        ]
                    }
                ],
                "tier0RoutingType":"EBGP",
                "tier0Name":"WLD01-T0",
                "tier1Name":"WLD01-T1",
                "edgeClusterProfileType":"DEFAULT"
                }
