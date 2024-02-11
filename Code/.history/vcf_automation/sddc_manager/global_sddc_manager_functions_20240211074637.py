import requests
import json
from requests.exceptions import RequestException
from requests.exceptions import HTTPError
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def monitor_sddc_manager_task(sddc_manager_ip, task_id, token):
    '''
    This function monitors the status of a task on the SDDC Manager
    '''
    url = f"https://{sddc_manager_ip}/v1/tasks/{task_id}"
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {token}'
      }
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response.json()