import os

from flask import Flask, session
# this imports flask from Flask library and then also imports the session

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
#modules used to set up authorization with spotipy library and therefore the spotify api



app = Flask(__name__) # creates a flask app and stores in app variable

app.config["Secret_Key"] = os.urandom(64) 
# generates a secret key so that users can't tamper with data inside session, ideally in production Secret_Key would be a fixed string
# but for now I'm just generating a random key each time

client_id = 'bffae03a1b6d42feacbc8f458a203362'
client_secret = 'bb801a548c08470c97fb2cf188d8fe23'
# IMPORTANT !!!!!!!
# ideally you would store these in environment variables or secured credential storage
# need to do that if pushed to production

redirect_uri = 'http://localhost:5000/callback'

#SCOPES FROM SDK AND WEB API MIGHT CAUSE ISSUES IF OCCURRED CONSIDER ONLY USING WEB API AND NOT SDK
scope = 'playlist-read-private, user-read-currently-playing'

cache_handler = FlaskSessionCacheHandler(session)
#creates flask session cache handler and imports the desired session

spotify_oauth = SpotifyOAuth(
    client_id= client_id,
    client_secret= client_secret,
    redirect_uri= redirect_uri,
    scope= scope,
    cache_handler = cache_handler,
    show_dialog= True


)

if __name__ == '__main__':
    app.run(debug = True)

