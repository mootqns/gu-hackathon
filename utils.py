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

def make_request(access_token, full_url):
    headers = {"Accept": "application/json", 
               "Content-Type": "application/json", 
               "Authorization": "Bearer " + access_token}

    response = requests.get(url=full_url, headers=headers)
    json_object = json.loads(response.text)

    return json_object

def search_request(access_token, search_term, search_type):
    search_term = requests.utils.quote(search_term)
    search_type = requests.utils.quote(search_type)
    url = secret.search_API_endpoint + "?q=" + search_term
    url += "&type=" + search_type
    print(url)
    json_obj = make_request(access_token, url)
    return json_obj

def get_ID(json_obj):
    tracks = json_obj["tracks"]
    items = tracks["items"]
    first_tracks_item = items[0]
    songID = first_tracks_item["id"]
    return songID

def get_track(access_token, id):
    headers = {"Accept": "application/json", 
               "Content-Type": "application/json", 
               "Authorization": "Bearer " + access_token}
    response = requests.get("https://api.spotify.com/v1/audio-features/"+id, headers=headers)
    json_object = json.loads(response.text)
    return json_object

def get_acousticness(access_token):
    access_token = get_access_token()
    # choosing taylor swift as a test artist to get her genres back
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    acousticness = track["acousticness"]
    return(acousticness)

def get_danceability(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    danceability = track["danceability"]
    return(danceability)

def get_duration_ms(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    duration_ms = track["duration_ms"]
    return(duration_ms)

def get_energy(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    energy = track["energy"]
    return(energy)

def get_instrumentalness(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    instrumentalness = track["instrumentalness"]
    return(instrumentalness)
    
def get_key(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    key = track["key"]
    return(key)

def get_liveness(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    liveness = track["liveness"]
    return(liveness)

def get_loudness(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    loudness = track["loudness"]
    return(loudness)

def get_speechiness(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    speechiness = track["speechiness"]
    return(speechiness)

def get_tempo(access_token, songID):
    json_obj = search_request(access_token, "Happy People", "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    tempo = track["tempo"]
    return(tempo)


if __name__ == "__main__":
    main()