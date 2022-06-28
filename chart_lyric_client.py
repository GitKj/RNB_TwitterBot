import requests
import os

LYRICS_URL = "http://api.chartlyrics.com//apiv1.asmx/SearchLyricDirect"


def get_song_metadata(artist: str, song_name: str):

    querystring = {"artist":artist,"song":song_name}

    headers = {
        "X-RapidAPI-Key": os.getenv("rapid_api_key"),
        "X-RapidAPI-Host": "sridurgayadav-chart-lyrics-v1.p.rapidapi.com"
    }

    return requests.request("GET", LYRICS_URL, headers=headers, params=querystring)
