import os


from flask import Flask, session, request, redirect, url_for
# this imports flask from Flask library and then also imports the session
# MIGHT NEED TO LOOK INTO IMPORTING REDIRECT AND REQUEST!!!!

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

app = Flask(__name__) # creates a flask app and stores in app variable

app.config["SECRET_KEY"] = os.urandom(64) 
# generates a secret key so that users can't tamper with data inside session, ideally in production Secret_Key would be a fixed string
# but for now I'm just generating a random key each time

client_id = 'bffae03a1b6d42feacbc8f458a203362'
client_secret = 'bb801a548c08470c97fb2cf188d8fe23'

redirect_uri = 'http://localhost:8000/callback'

scope = 'playlist-read-private, user-read-currently-playing, user-library-read, user-library-modify'

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

@app.route("/")
def home():
    user_input = input("What's an artist you like?: ")


    results = sp.search(q=user_input, type='artist')
    artist_id = results['artists']['items'][0]['id']  # Get the first artist ID

    # Define seeds
    seed_artists = [artist_id]  # Replace with actual artist IDs


    # Get recommendations
    recommendations = sp.recommendations(seed_artists=seed_artists)

    return("Ok here's some reccomendations based on the fact you like " + user_input)

    for track in recommendations['tracks']:
        return(f"Track: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
    # Print recommended tracks

if __name__ == "__main__":
    app.run(debug=True, port = 8000)