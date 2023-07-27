import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv

# Set the required parameters
client_id = 'your client id'
client_secret = 'your client secret'
redirect_uri = 'http://127.0.0.1:8888/callback'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
auth_url = sp_oauth.get_authorize_url()
sp = spotipy.Spotify(auth_manager=sp_oauth)


playlist_link = "https://open.spotify.com/playlist/6HzJErLbudz8EZew1bOw6r?si=8b1844f7d9f94dad"
csv_file = 'spotify_tracks.csv'


playlist_URI = playlist_link.split("/")[-1].split("?")[0]
fieldnames = ['Track URI', 'Track Name', 'Track Duration (ms)', 'Artist Name', 'Artist Popularity', \
              'Artist Genres', 'Album Name', 'Album Release Date', 'Track Popularity', 'Danceability', \
                'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', \
                    'Liveness', 'Valence', 'Tempo', 'Time Signature']
tracks_data = []
offset = 0
limit = 50
while True:
    playlist_tracks = sp.playlist_tracks(playlist_URI ,limit=limit,offset=offset)["items"]
    if len(playlist_tracks) == 0:
        break
    for track in playlist_tracks:
        # Extract track information
        track_uri = track["track"]["uri"]
        track_name = track["track"]["name"]
        track_duration_ms = track["track"]['duration_ms']
        
        # Extract artist information
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        artist_name = track["track"]["artists"][0]["name"]
        artist_popularity = artist_info["popularity"]
        artist_genres = ', '.join(artist_info["genres"])
        
        # Extract album information
        album_name = track["track"]["album"]["name"]
        album_release_date = track["track"]['album']['release_date']
        
        # Extract track popularity
        track_popularity = track["track"]["popularity"]
        
        # Extract track features
        track_features = sp.audio_features(track_uri)[0]
        danceability = track_features['danceability']
        energy = track_features['energy']
        key = track_features['key']
        loudness = track_features['loudness']
        mode = track_features['mode']
        speechiness = track_features['speechiness']
        acousticness = track_features['acousticness']
        instrumentalness = track_features['instrumentalness']
        liveness = track_features['liveness']
        valence = track_features['valence']
        tempo = track_features['tempo']
        time_signature = track_features['time_signature']
        
        track_data = {
            'Track URI': track_uri,
            'Track Name': track_name,
            'Track Duration (ms)': track_duration_ms,
            'Artist Name': artist_name,
            'Artist Popularity': artist_popularity,
            'Artist Genres': artist_genres,
            'Album Name': album_name,
            'Album Release Date': album_release_date,
            'Track Popularity': track_popularity,
            'Danceability': danceability,
            'Energy': energy,
            'Key': key,
            'Loudness': loudness,
            'Mode': mode,
            'Speechiness': speechiness,
            'Acousticness': acousticness,
            'Instrumentalness': instrumentalness,
            'Liveness': liveness,
            'Valence': valence,
            'Tempo': tempo,
            'Time Signature': time_signature
        }
        
        tracks_data.append(track_data)
    offset += limit

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(tracks_data)