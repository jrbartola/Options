from tdameritrade import TDClient
import os

TOKEN = os.environ.get('CLIENT_TOKEN')

if TOKEN is None:
    raise ValueError('CLIENT_TOKEN environment variable has not been set. Please set it to use the TDClient')

c = TDClient(TOKEN)
