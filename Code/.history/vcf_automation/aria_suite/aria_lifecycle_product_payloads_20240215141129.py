import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from aria_suite.aria_lifecycle.aria_lifecycle_functions import get_aria_life_cycle_datacenter, get_aria_lifecycle_certificate, create_aria_lifecycle_certificate,get_aria_lifecycle_license_keys_by_alias, create_aria_lifecycle_license_keys
from aria_suite.aria_lifecycle.aria_lifecycle_functions   import get_aria_lifecycle_dns, get_aria_lifecycle_locker_password, create_aria_lifecycle_locker_password
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
            "aria_suite_username": "admin",
            "aria_suite_password": "x9SyJnRR!",
            "deployment_network_properties": {
                    "network_name": "VM Network",
                    "portgroup": "vlan1024",
                    "gateway": "192.168.1.1",
                    "netmask": "255.255.255.0",
                    "domain": "seanlab.local",
                    "searchpath": "seanlab.local"
                    },
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
target_cluster_name = 'Main-Cluster'
aria_lifecycle_email = 'sean.e.gadson@gmail.com'
aria_enviornment_name = 'aria_enviornment_1'
products_ = {
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

license_key = '1234567890'
locker_username = 'admin'
locker_password = 'x9SyJnRR!'
aria_suite_datastore = 'management_domain_datastore'
deployment_network_properties_ = {
                    "network_name": "VM Network",
                    "portgroup": "vlan1024",
                    "gateway": "192.168.1.1",
                    "netmask": "255.255.255.0",
                    "domain": "seanlab.local",
                    "searchpath": "seanlab.local"
                    }
network = "VM Network"

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

    #Get Cluster Storage
    for item in target_cluster['storages']:
        if item['storageName'] == aria_suite_datastore:
            cluster_datastore = item
            break
    if cluster_datastore is None:
        raise Exception('Datastore not found')
    
    #Get Cluster Network Properties
    cluster_network_properties = deployment_network_properties_
     
    for item in target_cluster['networks']:
        if item['network'] == cluster_network_properties['network']:
            network = item['network'] 
            break
    if network is None:
        raise Exception('Network not found')

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
    
    products = products_

    #Get Aira Automation Hostnames and IP Addresses
    aria_automation_hostnames = []
    aria_automation_ip_addresses = []
   
    aria_automation = products['aria_automation']
    
    aria_automation_cluster_vip = aria_automation['clusterVIP']

    #Get Individual Cluster Nodes
    for node in aria_automation['nodes']:
        aria_automation_hostnames.append(node['name'])
        aria_automation_ip_addresses.append(node['ipAddress'])

    #Get Aira Operations Hostnames and IP Addresses
    aria_operations_hostnames = []
    aria_operations_ip_addresses = []
    
    aria_operations = products['aria_operations']
    
    aria_operations_cluster_vip = aria_operations['clusterVIP']
                                                  
    #Get Individual Cluster Nodes
    for node in aria_operations['nodes']:
        aria_operations_hostnames.append(node['name'])
        aria_operations_ip_addresses.append(node['ipAddress'])

    #Get Aira Operations Network Hostnames and IP Addresses
    aria_operations_network_hostnames = []
    aria_operations_network_ip_addresses = []
    
    aria_operations_network = products['aria_operations_network']
    
    aria_operations_network_cluster_vip = aria_operations_network['clusterVIP']

    #Get Individual Cluster Nodes
    for node in aria_operations_network['nodes']:
        aria_operations_network_hostnames.append(node['name'])
        aria_operations_network_ip_addresses.append(node['ipAddress'])

    #Get Aira Operations Logs Hostnames and IP Addresses
    aria_operations_logs_hostnames = []
    aria_operations_logs_ip_addresses = []

    aria_operations_logs = products['aria_operations_logs']
    
    aria_operations_logs_cluster_vip = aria_operations_logs['clusterVIP']

    #Get Individual Cluster Nodes
    for node in aria_operations_logs['nodes']:
        aria_operations_logs_hostnames.append(node['name'])
        aria_operations_logs_ip_addresses.append(node['ipAddress'])

    #Get Hostnames and IP Addresses
    hostnames = [aria_automation_hostnames, aria_operations_hostnames, aria_operations_network_hostnames, aria_operations_logs_hostnames, 
                 aria_automation_cluster_vip, aria_operations_cluster_vip, aria_operations_network_cluster_vip, 
                 aria_operations_logs_cluster_vip]
    ip_addresses = [aria_automation_ip_addresses, aria_operations_ip_addresses, aria_operations_network_ip_addresses, aria_operations_logs_ip_addresses,
                    aria_automation_cluster_vip, aria_operations_cluster_vip, 
                    aria_operations_network_cluster_vip, 
                    aria_operations_logs_cluster_vip]

    #Creating Product Alias
    product_alias = f'{aria_enviornment_name}'

    #Create or Get Certificate
    certificate = get_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias)

    if certificate is None:
        print('Certificate not found, creating certificate')
        
    certificate = create_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias, hostnames, ip_addresses)
    locker_certificate = f'locker:certificate:{certificate["vmid"]}:{product_alias}'
    #Create or Get License
    license = get_aria_lifecycle_license_keys_by_alias(aria_lifecycle_ip, product_alias)

    if license is None:
        print('License not found, creating license')
    
    license = create_aria_lifecycle_license_keys(aria_lifecycle_ip, product_alias, license_key)
    locker_license = f'locker:license:{license["vmid"]}:{product_alias}'

    #Create or Get Locker Password
    password = get_aria_lifecycle_locker_password(aria_lifecycle_ip, product_alias)

    if password is None:
        print('Password not found, creating password')
    
    password = create_aria_lifecycle_locker_password(aria_lifecycle_ip, product_alias, locker_username ,locker_password)

    locker_password = f'locker:password:{password["vmid"]}:{product_alias}'

    environment_details = {
        "license": locker_license,
        "environment_details_payload"  : {
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
        "defaultPassword": locker_password,
        "certificate": locker_certificate,
        "cluster": cluster_name,
        "storage": cluster_datastore,
        "folderName": "",
        "resourcePool": "",
        "diskMode": "thin",
        "network": network,
        "masterVidmEnabled": "false",
        "dns": dns_string,
        "domain": cluster_network_properties['domain'],
        "gateway": cluster_network_properties['gateway'],
        "netmask": cluster_network_properties['netmask'],
        "searchpath": cluster_network_properties['searchpath'],
        "timeSyncMode": "host",
        "ntp": "",
        "isDhcp": "false"
        }
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