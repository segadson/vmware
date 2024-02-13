import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from aria_lifecycle_functions import *

def get_aria_lifecycle_environment_details(*args, **kwargs):
    '''
    This function gets the environment details for Aria Lifecycle Product Deployment
    '''


    return environment_details

def create_workspace_one_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:
    - configuration_email: The default email address for the Workspace ONE configuration
    - admin_username: The password for the local admin account made from Locker
    - locker_password: The password for the local admin account made from Locker
    - node_size: The size of the node
    - server_certificate: The server certificate
    - locker_license: The license for the Locker
    '''
    server_properties = {}
    server_properties['defaultConfigurationEmail'] = configuration_email
    server_properties['defaultConfigurationUsername'] = admin_username
    server_properties['defaultConfigurationPassword'] = locker_password
    server_properties['vidmAdminPassword'] = locker_password
    server_properties['syncGroupMembers'] = False
    server_properties['nodeSize'] = node_size
    server_properties['defaultTenantAlias'] = ''
    server_properties['vidmDomainName'] = ''
    server_properties['certficicate'] = server_certificate
    server_properties['contentLibraryItemId'] = ''
    server_properties['licenseRef'] = locker_license

    # Workspace ONE Cluster Spec
    payload = {}
    payload['id'] = 'vidm'
    payload['version'] = product_version
    payload['properties'] = server_properties



    return payload

def create_aria_automation_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:

    '''
    payload = {}


    return payload

def create_aria_automation_config_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:

    '''
    payload = {}


    return payload

def create_aria_operations_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:

    '''
    payload = {}


    return payload

def create_aria_operations_networks_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:

    '''
    payload = {}


    return payload

def create_aria_operations_logs_payload(*args, **kwargs):
    '''
    This function creates the payload for Workspace ONE deployment in SDDC Manager
    Arguments:

    '''
    payload = {}


    return payload