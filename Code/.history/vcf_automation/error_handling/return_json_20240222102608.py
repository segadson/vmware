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
        print(response.json())
        logging.error(f'Connection Error: {e}')
        sys.exit(1)
        return None
    except requests.exceptions.Timeout as e:
        logging.error(f'Timeout Error: {e}')
        sys.exit(1)
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f'Request Exception: {e}')
        sys.exit(1)
        return None
    else:
        return response.json()