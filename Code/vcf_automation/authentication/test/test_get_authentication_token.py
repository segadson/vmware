import pytest
import requests
import json
import requests_mock
from get_authentication_token import get_vcf_token

def test_get_vcf_token(requests_mock):
    # Mock the requests.post method
    requests_mock.post('https://sddc-manager.vcf.sddc.lab/v1/tokens', json={'accessToken': 'mock_token'})

    # Call the function
    token = get_vcf_token()

    # Verify the response
    assert token == 'mock_token'