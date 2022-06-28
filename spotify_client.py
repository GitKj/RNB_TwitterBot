import config
import requests

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/playlists/'
LYRICS_URL = "http://api.chartlyrics.com//apiv1.asmx/SearchLyricDirect"
RNB_PLAYLIST_ID = "37i9dQZF1DWYmmr74INQlb"


def get_spotify_client():
    return requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': config.spotify_client_id,
        'client_secret': config.spotify_client_secret,
    })

def get_spotify_access_token():
    client_json_response = get_spotify_client().json()
    return client_json_response['access_token']


def make_playlist_request():
    access_token = get_spotify_access_token()
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    return requests.get(BASE_URL + RNB_PLAYLIST_ID + "/tracks?fields=items(track(name,artists.name))", headers=headers).json()
