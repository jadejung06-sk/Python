import requests
from bs4 import BeautifulSoup
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "03f6bf8e61be4f80986d5facbee40f8e"
CLIENT_SECRET = "6d83afb77a764a489dbdf0320c154ac7"
REDIRECT_URL = "https://example.com"

# ★
def login_spotipy():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope="playlist-modify-private", show_dialog= True, cache_path="./bs4_website/bs4_songs/token.txt"))
    user_id = sp.current_user()["id"]


def get_songs():
    ### real
    time = input("Which year do you want to travel to? Type the date in this format like 20000812:")
    THETIME = datetime.datetime.strptime(time, "%Y%m%d").date()
    year = THETIME.year
    # year = THETIME[:4] # ★
    ### test
    # THETIME = "2000-08-12"
    #########

    URL = f"https://www.billboard.com/charts/hot-100/{THETIME}/"
    response = requests.get(URL)
    HTML = response.text
    soup = BeautifulSoup(HTML, "html.parser")
    ### test
    # test = soup.find("h3", attrs = {"id":"title-of-a-story", "class": "c-title"})
    song_list = []
    title_text = soup.select("h3#title-of-a-story.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")
    for num in range(len(title_text)):
        # print(num+1, test[num].get_text().strip('\n\t'))
        songs = title_text[num].get_text().strip('\n\t')
        song_list.append(songs)
    return (song_list, THETIME)

if __name__ == "__main__":
    from spotipy.oauth2 import SpotifyClientCredentials
    from spotipy.oauth2 import SpotifyOAuth  
    import spotipy
    import sys
    import pprint
    import argparse
    import logging
    import datetime
    CLIENT_ID = "03f6bf8e61be4f80986d5facbee40f8e"
    CLIENT_SECRET = "6d83afb77a764a489dbdf0320c154ac7"
    REDIRECT_URL = "https://example.com"

    song_list = get_songs()
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope=scope, show_dialog= True, cache_path="./bs4_website/bs4_songs/token.txt"))
    user_id = sp.me()['id']
    # print(user_id) # 31owrzwiwgf6dcrns7xyp45a4ugu
   
    song_uris = []
    for song in song_list[0]:
        results = sp.search(q=f"track:{song} year:{song_list[1].year}", type="track")
        # print(results)
        try:
            uri = results["tracks"]["items"][0]["uri"]
            # print(uri)
            song_uris.append(uri)
        except IndexError:
            print(f"The song << {song} >> doesn't exist in Spotify. Pass")

    new_playlist = sp.user_playlist_create(user=user_id, name=f"{song_list[1]} Billboard 100", public= False)
    # print(new_playlist)
    billboard = sp.playlist_add_items(new_playlist["id"], items= song_uris)
    print(billboard)

# user_playlist_create
# playlist_add_items