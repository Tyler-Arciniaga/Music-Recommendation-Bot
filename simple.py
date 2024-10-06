import os

from flask import Flask, render_template, request, redirect, url_for
# this imports flask from Flask library and then also imports the session
# MIGHT NEED TO LOOK INTO IMPORTING REDIRECT AND REQUEST!!!!

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

app = Flask(__name__) # creates a flask app and stores in app variable

client_id = 'bffae03a1b6d42feacbc8f458a203362'
client_secret = 'bb801a548c08470c97fb2cf188d8fe23'

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods = ["POST"])
def process():
    artist_name = ''
    artist_name = request.form.get("artist_name")
    '''
    if request.method == "POST":
        artist_name = request.form.get("artist_name")
    '''
    return redirect(url_for('result', artist_name = artist_name))

@app.route('/result')
def result():
    artist_name = request.args.get('artist_name')
    results = sp.search(q=artist_name, type="artist")
    artist_id = results['artists']['items'][0]['id']  # Get the first artist ID
    seed_artists = [artist_id]  
    recommendations = sp.recommendations(seed_artists=seed_artists)
    
    for track in recommendations['tracks']:
        return(f"Track: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

   
if __name__ == "__main__":
    app.run(debug = True, port = 8000);