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
    ### test
    # THETIME = "2000-08-12"
    # print(THETIME)
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
    return song_list

if __name__ == "__main__":
    # song_list = get_songs()
    uri_query = {"track":"Wifey", 'year':2000}
    import spotipy

    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope="playlist-modify-private", show_dialog= True, cache_path="./bs4_website/bs4_songs/token.txt"))
    user_id = sp.current_user()["id"]

    artist = sp.artist(urn)
    print("artist:", artist)

    user = sp.user(user_id)
    print("user:", user)

    from spotipy.oauth2 import SpotifyClientCredentials
    import spotipy
    import sys
    import pprint

    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = {"track":"Wifey", 'year':2000, 'is_playable': True}

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URL, scope="playlist-modify-private", show_dialog= True, cache_path="./bs4_website/bs4_songs/token.txt"))
    
    result = sp.search(search_str, limit=1, type='track')
    pprint.pprint(result)