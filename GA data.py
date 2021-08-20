from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage
import json
import os
import re
import httplib2 
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
import requests
import pandas as pd

'''function check whether file exist in the path or not'''

def where_json(file_name):return os.path.exists(file_name)

def get_refresh_token(client_id,client_secret):
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'
    REDIRECT_URI = 'http:localhost:8080'
  
    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=SCOPE,redirect_uri=REDIRECT_URI)
    if where_json('credential.json')==False:
       storage = Storage('credential.json') 
       credentials = run_flow(flow, storage)
       refresh_token=credentials.refresh_token
       
    elif where_json('credential.json')==True:
       with open('credential.json') as json_file:  
           refresh_token=json.load(json_file)['refresh_token']
  
    return(refresh_token)
client_id = '920514126371-b3ajvg6ispv7e5aoo9aal79tn8r498k1.apps.googleusercontent.com'
client_secret = 'OY4S_GA60sDHS6WRMo5dIQyu'
refresh_token=get_refresh_token(client_id,client_secret)