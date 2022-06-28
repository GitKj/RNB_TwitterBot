import xml.etree.ElementTree as ET
from os import linesep
import re
import random
from twitter_client import get_Twitter_Client
from spotify_client import make_playlist_request
from chart_lyric_client import get_song_metadata
import time


# Getting playlist and choosing a random song from the list
def get_track_from_playlist():
    rnb_playlist = make_playlist_request()
    track_to_choose = random.randint(0, 39)
    track_chosen = rnb_playlist['items'][track_to_choose]
    artist = track_chosen['track']['artists'][0]['name']
    print(artist)
    song_name = track_chosen['track']['name']
    print(song_name)
    return artist, song_name


def get_song_lyrics(artist: str, song_name: str):
    raw_song_lyrics = get_song_metadata(artist, song_name)
    return clean_song_lyrics(raw_song_lyrics)
    

# Parsing the XML format, removing unnecessary spacing and blank lines
def clean_song_lyrics(response: str):
    regex_brackets_parenthesis = "[\(\[].*?[\)\]]"
    response_json = ET.fromstring(response.content)
    # The 9th "object" in the XML contains the lyrics
    raw_lyrics = response_json[9].text
    lyrics_parsed = re.sub(regex_brackets_parenthesis, "", raw_lyrics)
    return linesep.join([s for s in lyrics_parsed.splitlines() if s]).lstrip().splitlines()


def choose_lyrics_to_tweet(lyrics: str):
    num_sentences_in_lyrics = len(lyrics)
    lyrics_to_choose = random.randint(1, num_sentences_in_lyrics)
    lyric_sentence_1 = lyrics[lyrics_to_choose - 1].removesuffix(",").lstrip()
    lyric_sentence_2 = lyrics[lyrics_to_choose].removesuffix(",").lstrip()

    print(lyric_sentence_1)
    print(lyric_sentence_2)
    return lyric_sentence_1, lyric_sentence_2


def send_tweet(lyric_one: str, lyric_two: str, artist: str, song_name: str):
    client = get_Twitter_Client()
    lyrics_to_tweet = lyric_one + "\n" + lyric_two
    response = client.create_tweet(text=lyrics_to_tweet)

    print(f"https://twitter.com/user/status/{response.data['id']}")
    reply_tweet_with_artist_and_song(artist, song_name, response.data['id'])


def reply_tweet_with_artist_and_song(artist: str, song_name: str, tweet_id: str):
    client = get_Twitter_Client()
    client.create_tweet(in_reply_to_tweet_id=tweet_id, text=f"The name of the song is {song_name} by {artist}")


def main():

    # 4 hours is 14400
    while(True):
        artist, song_name = get_track_from_playlist()
        lyrics = get_song_lyrics(artist, song_name)
        lyric_one, lyric_two = choose_lyrics_to_tweet(lyrics)
        send_tweet(lyric_one, lyric_two, artist, song_name)
        time.sleep(14400)


if __name__ == "__main__":
    main()

