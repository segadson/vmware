import requests
import json
import logging
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from aria_suite.aria_lifecycle.aria_lifecycle_functions import get_aria_life_cycle_datacenter, get_aria_lifecycle_certificate, create_aria_lifecycle_certificate,get_aria_lifecycle_license_keys_by_alias, create_aria_lifecycle_license_keys
from aria_suite.aria_lifecycle.aria_lifecycle_functions   import get_aria_lifecycle_dns, get_aria_lifecycle_locker_password, create_aria_lifecycle_locker_password
from aria_suite.aria_lifecycle.aria_lifecycle_functions   import get_aria_lifecycle_ntp
from aria_suite.aria_lifecycle.aria_lifecycle_functions  import get_aria_lifecycle_datacenter_vcenter
from aria_suite.aria_lifecycle.dummy_payload import dummy_payload
from authentication.get_authentication_token import get_vcenter_token
from vcenter.vcenter_functions import get_vcenter_resource_pool
from sddc_manager.avns import *

'''
if vcf is true
for VCF Part:
"{\"vcfEnabled\":true,\"sddcManagerDetails\":[{\"sddcManagerHostName\":\"sfo-vcf01.sfo.rainpole.io\",\"sddcManagerName\":\"default\",\"sddcManagerVmid\":\"default\"}]}"
'''

def get_aria_lifecycle_environment_details(payload, aria_enviorments_name, *args, **kwargs):
    '''
    This function gets the environment details for Aria Lifecycle Product Deployment
    '''
    ######################################
    # Get environment details Vairables
    ######################################
    vcenter_ip = payload['aria_lifecycle']['deployment_vcenter']['hostname']
    vcenter_username = payload['aria_lifecycle']['deployment_vcenter']['username']
    vcenter_password = payload['aria_lifecycle']['deployment_vcenter']['password']

    aria_lifecycle_ip = payload['aria_lifecycle']['hostname']

    # for item in payload['aria_lifecycle']['aria_enviorments']:
    #     if item['name'] == aria_enviorments_name:
    #         aria_environment = item
    #         break
    # if aria_environment is None:
    #     raise Exception('Aria Environment not found')
    
    aria_environment = payload['aria_lifecycle']['aria_enviorments']
    
    target_datacenter = payload['aria_lifecycle']['deployment_datacenter']['name']
    target_vcenter_name_ = payload['aria_lifecycle']['deployment_vcenter']['name']
    target_cluster_name = aria_environment['aria_suite_cluster']
    target_vcenter_datacenter = payload['aria_lifecycle']['aria_enviorments']['deployment_vcenter_datacenter']
    aria_suite_datastore = aria_environment['aria_suite_datastore']
    aria_suite_username = aria_environment['aria_suite_username']
    aria_license_key = payload['aria_lifecycle']['license_key']
    aria_lifecycle_email = payload['aria_lifecycle']['aria_lifecycle_email']
    aria_suite_password = aria_environment['aria_suite_password']

    deployment_network_properties_ = aria_environment['deployment_network_properties']
    products_ = aria_environment['products']


    ######################################
    # Have To get Aria Environment Details
    ######################################

    vcenter_token = get_vcenter_token()
    #sddc_manager_token = get_vcf_token(sddc_manager_ip, sddc_manager_username, sddc_manager_password)
    target_datacenter = get_aria_life_cycle_datacenter(aria_lifecycle_ip, target_datacenter)
    target_datacenter_vmid = target_datacenter['dataCenterVmid']

    #Get Aria Lifecycle Datacenter vCenter Details
    target_vcenter = get_aria_lifecycle_datacenter_vcenter(aria_lifecycle_ip, target_datacenter['dataCenterName'], target_vcenter_name_)
    target_vcenter_host = target_vcenter['vCenterHost']
    target_vcenter_datacenters = target_vcenter['vCDataCenters']
    try:
        for item in target_vcenter_datacenters:
            if item['vcDataCenterName'] == target_vcenter_datacenter:
                target_vcenter_datacenter = item
                break
    except:
        raise Exception('Target Datacenter not found')
    
    target_vcenter_username = target_vcenter['vcUsername']
    target_vcenter_password = target_vcenter['vcPassword']
    
    try:
        for item in target_vcenter_datacenter['clusters']:
            if item['clusterName'] == target_cluster_name:
                target_cluster = item
                break
    except:
        raise Exception('Target Cluster not found')

    cluster_name = target_cluster['clusterName']


    #Get Cluster Storage
    try:
        for item in target_cluster['storages']:
            if item['storageName'] == aria_suite_datastore:
                cluster_datastore = item
                break
    except:
        raise Exception('Datastore not found')
    
    #Get Cluster Network Properties
    cluster_network_properties = deployment_network_properties_
    
    try:
        for item in target_cluster['networks']:
            if item['network'] == cluster_network_properties['network_name']:
                network = item['network'] 
                break
    except:
        raise Exception('Network not found')

    # #Get DNS and NTP
    dns = get_aria_lifecycle_dns(aria_lifecycle_ip)
    ntp = get_aria_lifecycle_ntp(aria_lifecycle_ip)

    dns_settings = []
    ntp_settings_array = []

    for item in dns:
        dns_settings.append(item['hostName'])

    dns_string = dns_settings

    # for item in ntp:
    #     ntp_settings_array.append(item['hostname'])
    
    # ntp_settings = ','.join(ntp_settings_array)
    
    products = products_

    #Get Aira Automation Hostnames and IP Addresses
    aria_automation_hostnames = []
    aria_automation_ip_addresses = []
   
    aria_automation = products['aria_automation']
    
    aria_automation_cluster_vip = aria_automation['clusterVIP']

    #Get Individual Cluster Nodes

    for node in aria_automation['nodes']:
        aria_automation_hostnames.append(node['properties']['hostname'])
        aria_automation_ip_addresses.append(node['properties']['ipAddress'])

    #Get Aira Operations Hostnames and IP Addresses
    aria_operations_hostnames = []
    aria_operations_ip_addresses = []
    
    aria_operations = products['aria_operations']
    
    aria_operations_cluster_vip = aria_operations['clusterVIP']
                                                  
    #Get Individual Cluster Nodes
    for node in aria_operations['nodes']:
        aria_operations_hostnames.append(node['properties']['hostname'])
        aria_operations_ip_addresses.append(node['properties']['ipAddress'])

    # #Get Aira Operations Network Hostnames and IP Addresses
    aria_operations_network_hostnames = []
    aria_operations_network_ip_addresses = []
    
    aria_operations_network = products['aria_operations_network']
    
    aria_operations_network_cluster_vip = aria_operations_network['clusterVIP']

    #Get Individual Cluster Nodes
    for node in aria_operations_network['nodes']:
        aria_operations_network_hostnames.append(node['properties']['hostname'])
        aria_operations_network_ip_addresses.append(node['properties']['ipAddress'])

    #Get Aira Operations Logs Hostnames and IP Addresses
    aria_operations_logs_hostnames = []
    aria_operations_logs_ip_addresses = []

    aria_operations_logs = products['aria_operations_logs']
    
    aria_operations_logs_cluster_vip = aria_operations_logs['clusterVIP']

    #Get Individual Cluster Nodes
    for node in aria_operations_logs['nodes']:
        aria_operations_logs_hostnames.append(node['properties']['hostname'])
        aria_operations_logs_ip_addresses.append(node['properties']['ipAddress'])

    #Get Hostnames and IP Addresses
    hostnames = aria_automation_hostnames + aria_operations_hostnames + aria_operations_network_hostnames + aria_operations_logs_hostnames
    print(aria_automation_cluster_vip)
    ip_addresses = aria_automation_ip_addresses + aria_operations_ip_addresses + aria_operations_network_ip_addresses + aria_operations_logs_ip_addresses + aria_automation_cluster_vip
    ip_addresses.append(aria_operations_cluster_vip, aria_operations_network_cluster_vip, aria_operations_logs_cluster_vip)

    #Creating Product Alias
    product_alias = f'{aria_enviorments_name}'

    #Create or Get Certificate
    try:
        certificate = get_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias)
    except:
        certificate = None
        print('Certificate not found, creating certificate')
        
    # certificate = create_aria_lifecycle_certificate(aria_lifecycle_ip, product_alias, hostnames, ip_addresses)
    # locker_certificate = f'locker:certificate:{certificate["vmid"]}:{product_alias}'
    # #Create or Get License
    # license = get_aria_lifecycle_license_keys_by_alias(aria_lifecycle_ip, product_alias)

    # if license is None:
    #     print('License not found, creating license')
    
    # license = create_aria_lifecycle_license_keys(aria_lifecycle_ip, product_alias, aria_license_key)
    # locker_license = f'locker:license:{license["vmid"]}:{product_alias}'

    # #Create or Get Locker Password
    # password = get_aria_lifecycle_locker_password(aria_lifecycle_ip, product_alias)

    # if password is None:
    #     print('Password not found, creating password')
    
    # password = create_aria_lifecycle_locker_password(aria_lifecycle_ip, product_alias, aria_suite_username ,aria_suite_password)

    # locker_password = f'locker:password:{password["vmid"]}:{product_alias}'

    # environment_details = {
    #     "license": locker_license,
    #     "environment_details_payload"  : {
    #     "dataCenterVmid": target_datacenter_vmid,
    #     "regionName": "default",
    #     "zoneName": "default",
    #     "vCenterName": target_vcenter_name,
    #     "vCenterHost": target_vcenter_host,
    #     "vcUsername": target_vcenter_username,
    #     "vcPassword": target_vcenter_password,
    #     "acceptEULA": True,
    #     "enableTelemetry": True,
    #     "adminEmail": aria_lifecycle_email,
    #     "defaultPassword": locker_password,
    #     "certificate": locker_certificate,
    #     "cluster": cluster_name,
    #     "storage": cluster_datastore,
    #     "folderName": "",
    #     "resourcePool": "",
    #     "diskMode": "thin",
    #     "network": network,
    #     "masterVidmEnabled": "false",
    #     "dns": dns_string,
    #     "domain": cluster_network_properties['domain'],
    #     "gateway": cluster_network_properties['gateway'],
    #     "netmask": cluster_network_properties['netmask'],
    #     "searchpath": cluster_network_properties['searchpath'],
    #     "timeSyncMode": "host",
    #     "ntp": "",
    #     "isDhcp": "false"
    #     }
    # }
    


    # return environment_details