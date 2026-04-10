import streamlit as st
import requests as req
#Goal: box that you input artist and you get similar artists and input song and you get similar songs

st.title("DJ Helper")
st.write("Welcome to DJ Helper! Enter a song and we will return a list of similar songs and similar artists to jumpstart your mixes! Customize artists and song popularity. We will do the rest!")

baseWebsite = "https://ws.audioscrobbler.com"
APIKey = "a37de3ee19ce5e9a0f8068415f2fa7b0"
track = st.text_input("input a song you want to mix", value=None)
artist = st.text_input("input the artist", value=None)
#if st.button("allow same artist"):
  #run code normally
#else:
  #if

def getSimilarTracks(artist, track):
  params = {
    "method": "track.getSimilar", 
    "artist": artist.replace(" ","+"),
    "track": track.replace(" ","+"),
    "apiKey": APIKey,
    "format": "json"
    "limit": 10
  }
  response = req.get(baseWebsite, params=params)
  data = response.json()

  tracks = []
  if "similartracks" in data:
    for t in data["similartracks"]["track"]:
      tracks.append(f"{t['name']}-{t['artist']['name']}")
      return tracks


def get_similar_artists(artist):
    params = {
        "method": "artist.getSimilar",
        "artist": artist,
        "api_key": APIKey,
        "format": "json",
        "limit": 10
    }
    response = requests.get(baseWebsite, params=params)
    data = response.json()
    
    artists = []
    if "similarartists" in data:
        for a in data["similarartists"]["artist"]:
            artists.append(a["name"])
    return artists

'''
f"https://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={artist}&track={track}&api_key=a37de3ee19ce5e9a0f8068415f2fa7b0&format=json
last.fm"

f"https://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key=a37de3ee19ce5e9a0f8068415f2fa7b0&format=json"


api code: a37de3ee19ce5e9a0f8068415f2fa7b0
http://www.last.fm/api/auth/?api_key=a37de3ee19ce5e9a0f8068415f2fa7b0
https://ws.audioscrobbler.com/2.0/?method=track.getInfo&artist=Bad+Bunny&track=La+Dificil&api_key=a37de3ee19ce5e9a0f8068415f2fa7b0&format=json
'''
baseWebsite = "https://ws.audioscrobbler.com"
APIKey = "a37de3ee19ce5e9a0f8068415f2fa7b0"
