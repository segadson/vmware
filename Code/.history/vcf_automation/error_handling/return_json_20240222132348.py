import time
import json
import os
import sys
import logging
import requests


    #     try:
    #         response.json() = response.json()['description']
    #         logging.error(f'HTTP Error: {e}')
    #         logging.error(f'Error Message: {response.json()}')
    #         sys.exit(1)
    #     except KeyError:
    #         response.json() = response.json()['value']['error_type']
    #         logging.error(f'HTTP Error: {e}')
    #         logging.error(f'Error Message: {response.json()}')
    #         sys.exit(1)
    #     return None
    # except requests.e

def return_json(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f'HTTP Error: {e}')
        logging.error(f'Error Message: {response.json()}')
        return None
    except requests.exceptions.ConnectionError as e:
        logging.error(f'HTTP Error: {e}')
        logging.error(f'Error Message: {response.json()}')
        return None
    except requests.exceptions.Timeout as e:
        logging.error(f'HTTP Error: {e}')
        logging.error(f'Error Message: {response.json()}')
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f'HTTP Error: {e}')
        logging.error(f'Error Message: {response.json()}')
        return None
    else:
        return response.json()