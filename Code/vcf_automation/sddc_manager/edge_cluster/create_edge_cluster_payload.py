import sys
sys.path.append('/Users/Administrator/vmware/Code/vcf_automation')

from authentication import get_authentication_token
# from sddc_manager.clusters import clusters_functions

# def create_edge_cluster_payload(sdd_manger_ip, vcf_token, domain_cluster_name):
#     '''
#     This function returns the payload for creating an edge cluster in SDDC Manager
#     '''

#     #Get Cluster ID for Edge Cluster Deployment
#     clusters = clusters_functions.get_sddc_manager_clusters(sdd_manger_ip, vcf_token)
#     for cluster in clusters['elements']:
#         if cluster['name'] == domain_cluster_name:
#             cluster_id = cluster['id']
#             break

#     if cluster_id is None:
#         raise SystemExit(f"Cluster {domain_cluster_name} not found in SDDC Manager")
    
#     payload = {
#     "asn": 65003,
#     "edgeAdminPassword": "VMware123!VMware123!",
#     "edgeAuditPassword": "VMware123!VMware123!",
#     "edgeRootPassword": "VMware123!VMware123!",
#     "mtu": 8940,
#     "tier0Name": "VLC-Tier-0",
#     "tier0RoutingType": "EBGP",
#     "tier0ServicesHighAvailability": "ACTIVE_ACTIVE",
#     "tier1Name": "VLC-Tier-1",
#     "edgeClusterName": "EC-01",
#     "edgeClusterProfileType": "DEFAULT",
#     "edgeClusterType": "NSX-T",
#     "edgeFormFactor": "LARGE",
#     "edgeNodeSpecs": [ {
#         "clusterId": "",
#         "edgeNodeName": "edge1-mgmt.vcf.sddc.lab",
#         "edgeTep1IP": "172.27.13.2/24",
#         "edgeTep2IP": "172.27.13.3/24",
#         "edgeTepGateway": "172.27.13.1",
#         "edgeTepVlan": 13,
#         "interRackCluster": false,
#         "managementGateway": "10.0.0.221",
#         "managementIP": "10.0.0.23/24",
#         "uplinkNetwork": [ {
#             "asnPeer": 65001,
#             "bgpPeerPassword": "VMware123!",
#             "peerIP": "172.27.11.1/24",
#             "uplinkInterfaceIP": "172.27.11.2/24",
#             "uplinkVlan": 11
#         },{
#             "asnPeer": 65001,
#             "bgpPeerPassword": "VMware123!",
#             "peerIP": "172.27.12.1/24",
#             "uplinkInterfaceIP": "172.27.12.2/24",
#             "uplinkVlan": 12
#         } ]
#     },{
#         "clusterId": cluster_id,
#         "edgeNodeName": "edge2-mgmt.vcf.sddc.lab",
#         "edgeTep1IP": "172.27.13.4/24",
#         "edgeTep2IP": "172.27.13.5/24",
#         "edgeTepGateway": "172.27.13.1",
#         "edgeTepVlan": 13,
#         "interRackCluster": False,
#         "managementGateway": "10.0.0.221",
#         "managementIP": "10.0.0.24/24",
#         "uplinkNetwork": [ {
#             "asnPeer": 65001,
#             "bgpPeerPassword": "VMware123!",
#             "peerIP": "172.27.11.1/24",
#             "uplinkInterfaceIP": "172.27.11.3/24",
#             "uplinkVlan": 11
#         },{
#             "asnPeer": 65001,
#             "bgpPeerPassword": "VMware123!",
#             "peerIP": "172.27.12.1/24",
#             "uplinkInterfaceIP": "172.27.12.3/24",
#             "uplinkVlan": 12
#         } ]
#     } ]
# }

#     return payload