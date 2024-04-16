import datetime

def format_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def handle_api_error(response):
    if response.status_code != 200:
        raise Exception(f'API request failed with status code {response.status_code}')
