# sddc_manager_wrapper/sddc_manager_domain.py
from sddc_manager_global_functions import get_vcf_token

token = get_vcf_token()
class Domain(object):
    def __init__(self, id, token):
        self.id = id
        self.token = token

    def info(self):
        return {'id': self.id}