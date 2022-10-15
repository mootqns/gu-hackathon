import secret
import json
import requests
import base64

# ---------------------
# GU Hackathon
# Utilities File
# ---------------------

def get_access_token():
    message = secret.client_ID + ":" + secret.client_secret
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    encoded_client_details = base64_bytes.decode("ascii")
    
    headers = {"Authorization": "Basic " + encoded_client_details}              
    body = {"grant_type": "client_credentials"}
    response = requests.post(url=secret.auth_endpoint, headers=headers, data=body)
    json_object = json.loads(response.text)
    return json_object["access_token"]
# function to load data
