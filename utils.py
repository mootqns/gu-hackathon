from webbrowser import get
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

def get_acousticness(track):
    acousticness = track["acousticness"]
    return(acousticness)

def get_danceability(track):
    danceability = track["danceability"]
    return(danceability)

def get_duration_ms(track):
    duration_ms = track["duration_ms"]
    return(duration_ms)

def get_energy(track):
    energy = track["energy"]
    return(energy)

def get_instrumentalness(track):
    instrumentalness = track["instrumentalness"]
    return(instrumentalness)
    
def get_key(track):
    key = track["key"]
    return(key)

def get_liveness(track):
    liveness = track["liveness"]
    return(liveness)

def get_loudness(track):
    loudness = track["loudness"]
    return(loudness)

def get_speechiness(track):
    speechiness = track["speechiness"]
    return(speechiness)

def get_tempo(track):
    tempo = track["tempo"]
    return(tempo)

def get_time_signature(track):
    time_signature = track["time_signature"]
    return(time_signature)

def get_track_info(access_token, name):
    json_obj = search_request(access_token, name, "track")
    songID = get_ID(json_obj)
    track = get_track(access_token, songID)
    acousticness = get_acousticness(track)
    danceability = get_danceability(track)
    duration_ms = get_duration_ms(track)
    energy = get_energy(track)
    instrumentalness = get_instrumentalness(track)
    key = get_key(track)
    liveness = get_liveness(track)
    loudness = get_loudness(track)
    speechiness = get_speechiness(track)
    tempo = get_tempo(track)
    time_signature = get_time_signature(track)







if __name__ == "__main__":
    main()