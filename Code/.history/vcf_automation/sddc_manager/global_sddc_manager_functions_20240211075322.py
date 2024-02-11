import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_sddc_manager_validation_status(sddc_manager_ip, vcf_token, validation_type, request_id):
    '''
    This function returns the validation status of SDDC Manager Component in VCF
    '''
    url = f"https://{sddc_manager_ip}/v1/{validation_type}/validations/{request_id}"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {vcf_token}'
      }
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()