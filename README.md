# Spotify Data Collection and Exploratory Data Analysis (EDA)

In this captivating project, I embarked on a musical journey by collecting data from my very own Spotify playlist and delving into the world of Exploratory Data Analysis (EDA). Here's a delightful step-by-step process to follow:

1. **Spotify Client ID and Client Secret:** Acquire your Spotify Client ID and Client Secret by following the guide at [this helpful link](https://support.heateor.com/get-spotify-client-id-client-secret/).

2. **Playlist Link:** Choose your preferred playlist on Spotify, click the share button, and copy the playlist link, which should be in the format "https://open.spotify.com/playlist/6HzJErLbudz8EZew1bOw6r?si=8b1844f7d9f94dad".

3. **Data Collection:** Utilize the `collect_data.py` script, fill in the `client_id`, `client_secret`, and `playlist_link` variables, and run the script to connect with your Spotify app. It fetches the delightful playlist data such as ['Track URI', 'Track Name', 'Track Duration (ms)', 'Artist Name', 'Artist Popularity', 'Artist Genres', 'Album Name', 'Album Release Date', 'Track Popularity', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Time Signature'], saving it gracefully in a CSV file.

4. **Data Cleanup:** The harmonious `notebook_cleanup.ipynb` sweetly cleans the collected data, retaining only the desired columns and gracefully removing any unusual values.

5. **Exploratory Data Analysis (EDA):** Embark on the rhythmic adventure with `notebook_eda.ipynb`, where delightful EDA awaits! Feel the beat of the distributions, dance with correlations, and savor the musical insights revealed by your curated Spotify playlist.

Dive into the immersive world of Jupyter Notebooks and CSV files in the repository, and let the music of data guide you through the splendid journey of your Spotify playlist!

*Note: Please handle your Spotify credentials with care and ensure data privacy while working on your personal Spotify playlist.*
