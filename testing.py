import argparse
import logging

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

client_id = 'bffae03a1b6d42feacbc8f458a203362'
client_secret = 'bb801a548c08470c97fb2cf188d8fe23'

redirect_uri = 'http://localhost:8000/callback'

scope = 'playlist-read-private, user-read-currently-playing, user-library-read, user-library-modify'

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

results = sp.search(q='Summrs', type='artist')
artist_id = results['artists']['items'][0]['id']  # Get the first artist ID

# Define seeds
seed_artists = [artist_id]  # Replace with actual artist IDs


# Get recommendations
recommendations = sp.recommendations(seed_artists=seed_artists)

# Print recommended tracks
for track in recommendations['tracks']:
    print(f"Track: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

