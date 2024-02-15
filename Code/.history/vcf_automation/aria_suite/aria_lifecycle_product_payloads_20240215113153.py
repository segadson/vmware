import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from aria_suite.aria_lifecycle.aria_lifecycle_functions import get_aria_life_cycle_datacenter, get_aria_lifecycle_certificate, create_aria_lifecycle_certificate
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
inputs = {
  "aria_lifecycle": {
    "hostname": "localhost",
    "ipAddress": "",
    "deployment_datacenter": {
        "name": "Default-VC",
        "primaryLocation": "Palo Alto;California;US;37.44188;-122.14302"
    },
    "deployment_vcenter":{
            "name": "Default-VC",
            "hostname": "bigdaddykingdom.seanlab.local",
            "username": "administrator@seanlab.local",
            "password": "x9SyJnRR!"
    },
    "aria_enviorments":[
        {
            "name": "aria_enviornment_1",
            "aria_suite_cluster": "Main-Cluster",
            "aria_suite_datastore": "Main-Datastore",
            "aria_suite_network": "Main-Network",
            "aria_suite_username": "admin",
            "aria_suite_password": "x9SyJnRR!",
                        "products": {
              "aria_automation": {
                "version:": "1.0.0",
                "clusterVIP": "",
                "collectorGroups": {
                  "name": "collector-group-1",
                  "operation": "add",
                  "collectors": [
                    {
                      "type": "remotecollector",
                      "name": "aria-suite-3",
                      "ipAddress": "",
                      "deployment_option": "smallrc"
                    },
                    {
                      "type": "cloudproxy",
                      "name": "aria-suite-4",
                      "ipAddress": "",
                      "deployment_option": "smallcp"
                    }
                  ]
                },
                "nodes": [
                  {
                    "type": "vrava-primary",
                    "name": "aria-automation-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrava-secondary",
                    "name": "aria-automation-2",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrava-secondary",
                    "name": "aria-automation-3",
                    "ipAddress": ""
                  }
                ]
              },
              "aria_operations": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "master",
                    "name": "aria-suite-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "replica",
                    "name": "aria-suite-2",
                    "ipAddress": ""
                  },
                  {
                    "type": "remotecollector",
                    "name": "aria-suite-3",
                    "ipAddress": "",
                    "deployment_option": "smallrc"
                  },
                  {
                    "type": "cloudproxy",
                    "name": "aria-suite-4",
                    "ipAddress": "",
                    "deployment_option": "smallcp"
                  }
                ]
              },
              "aria_operations_network": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "vrni-platform",
                    "name": "aria-suite-1",
                    "ipAddress": "",
                    "vrni_node_size": "small"
                  },
                  {
                    "type": "vrni-collector",
                    "name": "aria-suite-2",
                    "ipAddress": "",
                    "vrni_node_size": "small"
                  }
                ]
              },
              "aria_operations_logs": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "vrli-master",
                    "name": "aria-suite-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrli-worker",
                    "name": "aria-suite-2",
                    "ipAddress": ""
                  }
                ]
              }
            }
        }
    ]
  }
}

vcenter_ip = 'bigdaddykingdom.seanlab.local'
vcenter_username = 'administrator@seanlab.local'
vcenter_password = 'x9SyJnRR!'
aria_lifecycle_ip = 'local-vrlcm.seanlab.local'
target_datacenter = 'Default-DC'
target_vcenter_name = 'Default-VC'
aria_lifecycle_email = 'sean.e.gadson@gmail.com'
aria_enviornment_name = 'aria_enviornment_1'


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
    target_datacenter_vmiid = target_datacenter['dataCenterVmid']

    #Get Aria Lifecycle Datacenter vCenter Details
    target_vcenter = get_aria_lifecycle_datacenter_vcenter(aria_lifecycle_ip, target_datacenter, target_vcenter_name)
    target_vcenter_name = target_vcenter['vCenterHost']
    target_vcenter_username = target_vcenter['vcUsername']
    target_vcenter_password = target_vcenter['vcPassword']
    
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

    #Get Hostnames and IP Addresses
    hostnames = []
    ip_addresses = []

    #Creating Product Alias
    product_alias = f'{aria_enviornment_name}'

    #Create or Get Certificate
    certificate = get_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias)

    if certificate is None:
        print('Certificate not found, creating certificate')
        
    certificate = create_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias, hostnames, ip_addresses)
    #Create or Get License

    #Create or Get Locker Password


    environment_details = {
      "dataCenterVmid": target_datacenter_vmiid,
      "regionName": "default",
      "zoneName": "default",
      "vCenterName": target_vcenter_name,
      "vCenterHost": target_vcenter_name,
      "vcUsername": target_vcenter_username,
      "vcPassword": target_vcenter_password,
      "acceptEULA": True,
      "enableTelemetry": True,
      "adminEmail": aria_lifecycle_email,
      "defaultPassword": "locker:password:81fb2ee9c5bb:VMware1!",
      "certificate": "locker:certificate:49b8ff35b0a:vm",
      "cluster": "Datacenter#Cluster-01",
      "storage": "ISCSI-15TB-04",
      "folderName": "",
      "resourcePool": "",
      "diskMode": "thin",
      "network": "infra-traffic-1024",
      "masterVidmEnabled": "false",
      "dns": "10.141.66.213,10.118.183.252",
      "domain": "sqa.local",
      "gateway": "10.196.57.253",
      "netmask": "255.255.254.0",
      "searchpath": "sqa.local",
      "timeSyncMode": "host",
      "ntp": "",
      "isDhcp": "false"
    }
    


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