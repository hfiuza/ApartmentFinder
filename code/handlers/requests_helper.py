import sys
import time
import requests


def make_get_request(url, max_retries=15):
    return request_with_retry(lambda url: requests.get(url), max_retries, url)


def request_with_retry(request_method, max_retries, *args, **kwargs):
    wait = 1
    retries = 0
    while retries < max_retries:
        try:
            response = request_method(*args, **kwargs)
            break
        except Exception:
            wait *= 2
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            retries += 1

    return response if retries < max_retries else None
