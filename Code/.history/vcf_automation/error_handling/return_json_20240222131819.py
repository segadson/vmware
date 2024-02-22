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
        print(response.json())
        try:
            error_message = response.json()['description']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        except KeyError:
            error_message = response.json()['value']['error_type']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        return None
    except requests.exceptions.ConnectionError as e:
        try:
            error_message = response.json()['description']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        except KeyError:
            error_message = response.json()['value']['error_type']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        return None
    except requests.exceptions.Timeout as e:
        try:
            error_message = response.json()['description']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        except KeyError:
            error_message = response.json()['value']['error_type']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        return None
    except requests.exceptions.RequestException as e:
        try:
            error_message = response.json()['description']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        except KeyError:
            error_message = response.json()['value']['error_type']
            logging.error(f'HTTP Error: {e}')
            logging.error(f'Error Message: {error_message}')
            sys.exit(1)
        return None
    else:
        return response.json()