import streamlit as st
import requests
#Goal: box that you input artist and you get similar artists and input song and you get similar songs

st.title("DJ Helper")
st.write("Welcome to DJ Helper! Enter a song and we will return a list of similar songs and similar artists to jumpstart your mixes! Customize artists and song popularity. We will do the rest!")

#Base URL and API Key

baseUrl = 'http://ws.audioscrobbler.com/2.0'
apiKey = "a28edaddcd62a1f9f8ae8100299fbc3b"

###Similar Artists Function:

def getSimilarArtists(inputArtist):

    #Endpoint code:

    addBaseArtisturl = baseUrl + "/?method=artist.getsimilar&artist="
    urlArtist = inputArtist.replace(" ", "+")
    endpoint1 = addBaseArtisturl + urlArtist + "&api_key=" + apiKey + "&format=json"
    response1 = requests.get(endpoint1)

    #Return the list code:

    try:
        data1 = response1.json()
        similarArtistList = []
        for i in data1["similarartists"]["artist"]:
            if float(i["match"]) <= 1 and float(i["match"]) >= .5:
                similarArtistList.append(i["name"])
        return similarArtistList[:10]
    
    except:
        return "Bad response. Try capitalizing the artist name."

###Similar Songs Function:

def getSimilarSongs(inputSong, inputArtist):

    #Endpoint code:
    
    urlArtist = inputArtist.replace(" ", "+")
    addBaseSongurl = baseUrl + "/?method=track.getsimilar&artist=" + urlArtist
    urlSong = inputSong.replace(" ", "+")
    endpoint2 = addBaseSongurl + "&track=" + urlSong + "&api_key=" + apiKey + "&format=json"
    response2 = requests.get(endpoint2)

    #Return the list code:

    try:
        data2 = response2.json()
        similarSongList = []
        for i in data2["similartracks"]["track"]:
            if float(i["match"]) <= 1 and float(i["match"]) >= .5:
                similarSongList.append(i["name"])
        return similarSongList[:10]
    
    except:
        return "Bad response"

with st.form("survey_form"):
    inputSong = st.text_input("input a song you want to mix", value=None)
    inputArtist = st.text_input("input the artist", value=None)
    submitted = st.form_submit_button("Submit Data")
    if submitted:
        st.write("**You may like these artists:**")
        for a in getSimilarArtists(inputArtist):
            st.write(f"{a}")
        st.write("**You may like these songs:**")
        for p in getSimilarSongs(inputSong, inputArtist):
            st.write(f"{p}")
        st.write(getSimilarSongs(inputSong, inputArtist))

'''
if st.button("change up the artists"):
    if float(i["artist"]["name"]) != inputArtist:
        similarSongList.append(i["name"])
else:
                  dont run
if st.button("popular songs only"):
    if float(i["playcount"]) > 10000:
        similarSongList.append(i["name"])
else:
    dont run
'''