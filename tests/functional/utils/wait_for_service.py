import time

import requests

from tests.functional.settings import test_settings

if __name__ == '__main__':
    while True:
        try:
            response = requests.get(test_settings.app_url + '/api/ping')
            break
        except requests.ConnectionError:
            time.sleep(1)
