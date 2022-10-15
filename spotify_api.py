# @author Gina Sprint
# Get Genre for Searched Artist Name
# Get access token: https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
# Search for artist: https://developer.spotify.com/documentation/web-api/reference/search/search/

import requests
import json 
import base64

# TODO: move these into a file/environment variable external to the code
client_ID = "27d9f488070742d2aef19da110262941"
client_secret = "e25970d2f33740a6a49bb06866abf20b"

auth_endpoint = "https://accounts.spotify.com/api/token"
search_API_endpoint = "https://api.spotify.com/v1/search"

# get access token to use for authentication with search api
def get_access_token():
    # from Spotify docs:
    # Required: Base 64 encoded string that contains the client ID and client secret key. 
    # The field must have the format: 
    # Authorization: Basic *<base64 encoded client_id:client_secret>*
    message = client_ID + ":" + client_secret
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    encoded_client_details = base64_bytes.decode("ascii")
    
    headers = {"Authorization": "Basic " + encoded_client_details}              
    body = {"grant_type": "client_credentials"}
    response = requests.post(url=auth_endpoint, headers=headers, data=body)
    json_object = json.loads(response.text)
    return json_object["access_token"]
    
# make the request using requests module
# need to send the access token via request headers
def make_request(access_token, full_url):
    headers = {"Accept": "application/json", 
               "Content-Type": "application/json", 
               "Authorization": "Bearer " + access_token}

    response = requests.get(url=full_url, headers=headers)
    json_object = json.loads(response.text)

    return json_object

# create request url, make request, return JSON response
def search_request(access_token, search_term, search_type):
    search_term = requests.utils.quote(search_term)
    search_type = requests.utils.quote(search_type)
    url = search_API_endpoint + "?q=" + search_term
    url += "&type=" + search_type
    print(url)
    json_obj = make_request(access_token, url)
    return json_obj

# parse list of genres from JSON response
def get_genres(json_obj):
    artists = json_obj["artists"]
    items = artists["items"]
    first_artist_item = items[0] # TODO: are they sorted by match confidence/popularity?
    genres = first_artist_item["genres"]
    return genres

# fire 'er off!!
def main():
    access_token = get_access_token()
    # choosing taylor swift as a test artist to get her genres back
    json_obj = search_request(access_token, "bon iver", "artist")
    genres = get_genres(json_obj)
    print("genres:", genres)

main()

# output
# https://api.spotify.com/v1/search?q=taylor%20swift&type=artist
# taylor swift's genres: ['pop']