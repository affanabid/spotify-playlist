import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import time

# Set up your Client ID, Client Secret, and Redirect URI
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://example.com'  # Must match the Redirect URI you set in the Spotify Developer Dashboard

# Create the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='')

# Check if a token file already exists
token_info = None
if os.path.isfile("token.txt"):
    with open("token.txt", "r") as token_file:
        token = token_file.read()
    token_info = {'access_token': token}

# Check if the token is expired or not
if not token_info or 'expires_at' not in token_info or token_info['expires_at'] < int(time.time()):
    # Get the authorization URL
    auth_url = sp_oauth.get_authorize_url()

    # Redirect the user to the authorization URL
    print(f'Please visit this URL to authorize the application: {auth_url}')

    # After authorization, retrieve the authorization code from the redirected URL
    code = input('Enter the authorization code from the URL: ')

    # Exchange the authorization code for an access token
    token_info = sp_oauth.get_access_token(code)

    # Save the token information to a file
    with open("token.txt", "w") as token_file:
        token_file.write(token_info['access_token'])

# Create a Spotify client object
sp = spotipy.Spotify(auth=token_info['access_token'])

# Now you can use the Spotify client object to interact with the Spotify API
# For example, let's get the current user's profile information
current_user = sp.current_user()
user_id = current_user['id']

print(f"Authenticated user's Spotify username: {user_id}")
