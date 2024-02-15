import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from aria_suite.aria_lifecycle.aria_lifecycle_functions import get_aria_life_cycle_datacenter
from aria_suite.aria_lifecycle.aria_lifecycle_functions   import get_aria_lifecycle_dns
from aria_suite.aria_lifecycle.aria_lifecycle_functions   import get_aria_lifecycle_ntp
from aria_suite.aria_lifecycle.aria_lifecycle_functions  import get_aria_lifecycle_datacenter_vcenter
from authentication.get_authentication_token import get_vcenter_token
from vcenter.vcenter_functions import get_vcenter_resource_pool
from sddc_manager.avns import *

'''
if vcf is true
for VCF Part:
"{\"vcfEnabled\":true,\"sddcManagerDetails\":[{\"sddcManagerHostName\":\"sfo-vcf01.sfo.rainpole.io\",\"sddcManagerName\":\"default\",\"sddcManagerVmid\":\"default\"}]}"
'''

vcenter_ip = 'bigdaddykingdom.seanlab.local'
vcenter_username = 'administrator@seanlab.local'
vcenter_password = 'x9SyJnRR!'
aria_lifecycle_ip = 'local-vrlcm.seanlab.local'
target_datacenter = 'Default-DC'
target_vcenter_name = 'Default-VC'

def get_aria_lifecycle_environment_details(*args, **kwargs):
    '''
    This function gets the environment details for Aria Lifecycle Product Deployment
    '''
    ######################################
    # Have To get Aria Environment Details
    ######################################

    vcenter_token = get_vcenter_token(vcenter_ip, vcenter_username, vcenter_password)
    #sddc_manager_token = get_vcf_token(sddc_manager_ip, sddc_manager_username, sddc_manager_password)
    target_datacenter = get_aria_life_cycle_datacenter(aria_lifecycle_ip, target_datacenter)

    #Get Aria Lifecycle Datacenter vCenter Details
    target_vcenter = get_aria_lifecycle_datacenter_vcenter(aria_lifecycle_ip, target_datacenter, target_vcenter_name)
    
    for item in target_vcenter['clusters']:
        if item['clusterName'] == target_cluster_name:
            target_cluster = item
            break
    if target_cluster is None:
        raise Exception('Target Cluster not found')
    
    cluster_name = f'{target_vcenter["vCDatacenterName"]}#{target_cluster["clusterName"]}'

    #Get vCenter Resource Group
    vcenter_resource_group = get_vcenter_resource_pool(vcenter_ip, vcenter_token, cluster_name)

    #Get DNS and NTP
    dns = get_aria_lifecycle_dns(aria_lifecycle_ip)
    ntp = get_aria_lifecycle_ntp(aria_lifecycle_ip)

    dns_settings = []
    ntp_settings_array = []

    for item in dns:
        dns_settings.append(item['hostname'])

    dns_string = f'{dns_settings[0]},{dns_settings[1]}'

    for item in ntp:
        ntp_settings_array.append(item['hostname'])
    
    ntp_settings = ','.join(ntp_settings_array)

    #Create or Get Certificate
    #Create or Get License
    #Create or Get Locker Password


    environment_details = {}
    


    return environment_details

# def create_workspace_one_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:
#     - configuration_email: The default email address for the Workspace ONE configuration
#     - admin_username: The password for the local admin account made from Locker
#     - locker_password: The password for the local admin account made from Locker
#     - node_size: The size of the node
#     - server_certificate: The server certificate
#     - locker_license: The license for the Locker
#     '''
#     server_properties = {}
#     server_properties['defaultConfigurationEmail'] = configuration_email
#     server_properties['defaultConfigurationUsername'] = admin_username
#     server_properties['defaultConfigurationPassword'] = locker_password
#     server_properties['vidmAdminPassword'] = locker_password
#     server_properties['syncGroupMembers'] = False
#     server_properties['nodeSize'] = node_size
#     server_properties['defaultTenantAlias'] = ''
#     server_properties['vidmDomainName'] = ''
#     server_properties['certficicate'] = server_certificate
#     server_properties['contentLibraryItemId'] = ''
#     server_properties['licenseRef'] = locker_license

#     # Workspace ONE Cluster Spec
#     payload = {}
#     payload['id'] = 'vidm'
#     payload['version'] = product_version
#     payload['properties'] = server_properties



#     return payload

# def create_aria_automation_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:

#     '''
#     payload = {}


#     return payload

# def create_aria_automation_config_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:

#     '''
#     payload = {}


#     return payload

# def create_aria_operations_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:

#     '''
#     payload = {}


#     return payload

# def create_aria_operations_networks_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:

#     '''
#     payload = {}


#     return payload

# def create_aria_operations_logs_payload(*args, **kwargs):
#     '''
#     This function creates the payload for Workspace ONE deployment in SDDC Manager
#     Arguments:

#     '''
#     payload = {}


#     return payload