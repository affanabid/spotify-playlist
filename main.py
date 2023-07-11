from bs4 import BeautifulSoup
import requests, spotipy
from spotipy.oauth2 import SpotifyClientCredentials

USERNAME = '31ptcy4eolphg3dsdfzyquc6nwcu'
CLIENT_ID = '13318f4c7344424c836141c9eece92d4'
CLIENT_SECRET = 'c7d46966d2b64efbb25286ec2e58b69b'
REDIRECT_URI = 'http://example.com'
SCOPE = 'playlist-modify-public'
user_date = input('Which year do you want to travel? Type the date in this format YYYY-MM-DD: ')
PLAYLIST_NAME = f'{user_date} Billboard 100'

# creates a list of of top 100 music tracks of the user-given date
def create_music_list(user_date):
    music = []
    response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{user_date}/')
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all(class_='o-chart-results-list-row-container')
    for row in rows:
        title = row.find(name='h3', id='title-of-a-story').getText().strip()
        music.append(title)
    return music

# creates a list of URIs from the list of tracks
def create_uri_list(CLIENT_ID, CLIENT_SECRET, music_list):
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    song_uri_list = []
    for music in music_list:
        result = sp.search(q=f'{music}', type='track', limit=1)
        if len(result['tracks']['items']) > 0:
            song_uri = result['tracks']['items'][0]['uri']
            song_uri_list.append(song_uri)
    return song_uri_list

# creates a playlist with the name of user-given date
def create_playlist(USERNAME, PLAYLIST_NAME):
    playlist = sp.user_playlist_create(USERNAME, name=PLAYLIST_NAME)
    return playlist['id']

# search the songs in spotify through their URIs and adds them to the created playlist
def add_to_playlist(PLAYLIST_ID, tracks_list):
    sp.playlist_add_items(playlist_id=PLAYLIST_ID,items=tracks_list, position=None)

music_list = create_music_list(user_date)
song_uri_list = create_uri_list(CLIENT_ID, CLIENT_SECRET, music_list)
token = spotipy.util.prompt_for_user_token(username=USERNAME,scope=SCOPE,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI) 
sp = spotipy.Spotify(auth=token)
playlist_id = create_playlist(USERNAME, PLAYLIST_NAME)
add_to_playlist(playlist_id, song_uri_list)