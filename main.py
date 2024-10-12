import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, redirect, url_for,render_template_string
# this imports flask from Flask library and then also imports the session
# MIGHT NEED TO LOOK INTO IMPORTING REDIRECT AND REQUEST!!!!

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

app = Flask(__name__) # creates a flask app and stores in app variable
load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

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

   # return recommendations
    track_list = []
    
    
    for track in recommendations['tracks']:
        track_info = (f"Track: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
        track_list.append(track_info)


    html_content = '<br>'.join(track_list)
    return render_template("results.html", tracks = track_list, artist_name = artist_name)
    #return render_template_string("<h1>Track List</h1><p>{}</p>".format(html_content))

if __name__ == "__main__":
    app.run(debug = True, port = 8000);