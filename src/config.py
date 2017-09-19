import os
import sys

def get_access_token():
    if os.environ.get('ACCESS_TOKEN') is None:
        print('ERROR: No ACCESS_TOKEN environment variable set.')
        print('Once you have obtained your access token from Companies house, you can set the environment variable by '
              'executing \'setx ACCESS_TOKEN "<your access token here>" /m \' at a command prompt')
        exit(1)
    else:
        return os.environ['ACCESS_TOKEN']

data_filepath = "data/fresh_data.json"
data_cache_filepath = "data/cached_data.json"
