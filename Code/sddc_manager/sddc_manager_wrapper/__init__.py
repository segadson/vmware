# sddc_manager_wrapper/__init__.py
from sddc_manager_global_functions import get_vcf_token
import requests

SDDC_API_TOKEN = get_vcf_token()

class APIKeyMissingError(Exception):
    pass

if SDDC_API_TOKEN is None:
    raise APIKeyMissingError(
        "All methods require an API key."
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = SDDC_API_TOKEN

from .sddc_manager_domain import Domain
