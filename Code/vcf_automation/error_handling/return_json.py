import time
import json
import os
import sys
import logging
import requests


def return_json(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_message = response.json()['description']
        logging.error(f'HTTP Error: {e}')
        logging.error(f'Error Message: {error_message}')
        sys.exit(1)
        return None
    except requests.exceptions.ConnectionError as e:
        error_message = response.json()['description']
        logging.error(f'Connection Error: {e}')
        logging.error(f'Error Message: {error_message}')
        sys.exit(1)
        return None
    except requests.exceptions.Timeout as e:
        error_message = response.json()['description']
        logging.error(f'Timeout Error: {e}')
        logging.error(f'Error Message: {error_message}')
        sys.exit(1)
        return None
    except requests.exceptions.RequestException as e:
        error_message = response.json()['description']
        logging.error(f'Request Exception: {e}')
        logging.error(f'Error Message: {error_message}')
        sys.exit(1)
        return None
    else:
        return response.json()