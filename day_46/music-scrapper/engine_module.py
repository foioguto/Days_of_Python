import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

class Engine:
    def __init__(self, date, url):
        self.date = date
        self.url = url

    def __str__(self):
        return f"{self.date}"

    def scrap(self):
        response = requests.get(self.url)
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")
        song_names_spans = soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in song_names_spans]

        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope= "playlist-modify-private",
                redirect_uri= os.getenv("SPOTIPY_REDIRECT_URI"),
                client_id = os.getenv("CLIENT_ID"),
                client_secret = os.getenv("CLIENT_SECRET"),
                show_dialog = True,
                cache_path = "token.txt",
            )
        )

        user_id = sp.current_user()["id"]
        song_uris = []
        year = self.date.split("-")[0]

        for song in song_names:
            result = sp.search(q=f"track:{song} year:{year}", type="track", limit=5)
            if result["tracks"]["items"]:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            else:
                print(f"Song '{song}' not found on Spotify.")

        playlist = sp.user_playlist_create(user=user_id, name=f"{self.date} Billboard 100", public=False)
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
