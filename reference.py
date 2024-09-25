import os

from flask import Flask, session, request, redirect, url_for
# this imports flask from Flask library and then also imports the session
# MIGHT NEED TO LOOK INTO IMPORTING REDIRECT AND REQUEST!!!!

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
#modules used to set up authorization with spotipy library and therefore the spotify api



app = Flask(__name__) # creates a flask app and stores in app variable

app.config["SECRET_KEY"] = os.urandom(64) 
# generates a secret key so that users can't tamper with data inside session, ideally in production Secret_Key would be a fixed string
# but for now I'm just generating a random key each time

client_id = 'bffae03a1b6d42feacbc8f458a203362'
client_secret = 'bb801a548c08470c97fb2cf188d8fe23'
# IMPORTANT !!!!!!!
# ideally you would store these in environment variables or secured credential storage
# need to do that if pushed to production

redirect_uri = 'http://localhost:8000/callback'
## requires a port that isn't 5000 (for some reason this port has some conflict on mac so I used 8000 instead)

#SCOPES FROM SDK AND WEB API MIGHT CAUSE ISSUES IF OCCURRED CONSIDER ONLY USING WEB API AND NOT SDK
scope = 'playlist-read-private, user-read-currently-playing, user-library-read'

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
sp = Spotify(auth_manager=spotify_oauth) #creates an instance of the spotify client using out auth manager



@app.route('/') #defines root for web application in flask #when user types slash it takes you to homepage
def home():
    if not spotify_oauth.validate_token(cache_handler.get_cached_token()): #if user hasn't logged in we want them to log in w spotify (validate_token returns false)
        auth_url = spotify_oauth.get_authorize_url() # takes user to "Login with Spotify page" page (done by calling get_authorize_url())
        return redirect(auth_url) #returns that redirect url and therefore redirects user to desired page
    return redirect(url_for('get_playlists')) #requires user to have a valid token, then redirects to "get playlists" endpoint


@app.route('/callback') #after user logs in successfully with spotify spotify comes to callback API endpoint
def callback():
    spotify_oauth.get_access_token(request.args['code']) #spotify gives us a code
    
    return redirect(url_for('Taylor')) 
    #stores spotify given code and then uses to get and refresh access token
    #what this does is allows users to only have to log in once (will require to login again if scope is changed)
    #also redirects to get_playlists endpoint

@app.route('/get_playlists')
def get_playlists():
    if not spotify_oauth.validate_token(cache_handler.get_cached_token()): #if user hasn't logged in we want them to log in w spotify (validate_token returns false)
        auth_url = spotify_oauth.get_authorize_url() # takes user to "Login with Spotify page" page (done by calling get_authorize_url())
        return redirect(auth_url) #returns that redirect url and therefore redirects user to desired page

    playlists = sp.current_user_playlists() #calls spoitfy api function to get user playlists
    playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']] # creates a list for playlist with playlist being an "item" key
    playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])

    return playlists_html 

@app.route('/Taylor')
def get_taylor():
    taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

    results = sp.artist_albums(taylor_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
#might need to be url_for('/home')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
    # sets port equal to 8000 because 5000 is the default, but port 5000 has conflict on macbook

