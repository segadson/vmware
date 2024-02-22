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
        logging.error(f'HTTP Error: {e}')
        return None
    except requests.exceptions.ConnectionError as e:
        logging.error(f'Connection Error: {e}')
        return None
    except requests.exceptions.Timeout as e:
        logging.error(f'Timeout Error: {e}')
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f'Request Exception: {e}')
        return None
    else:
        return response.json()