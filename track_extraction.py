"""THIS IS FOR TOP 50 SONGS IN DIFFERENT COUNTRIES/AREAS"""
import sqlite3
import pytz
import spotipy
import pandas as pd
import datetime
import sqlalchemy
import Authorization

sp = spotipy.Spotify(client_credentials_manager=Authorization.client_credentials_manager)

# EDM hits
EDM_HITS = "37i9dQZF1DX1kCIzMYtzum"
LOFI_BEATS = "37i9dQZF1DWWQRwui0ExPn"


def get_URI(playlist):
    if playlist.startswith("https://api.spotify.com/v1/playlists/") | playlist.startswith(
            "https://open.spotify.com/playlist/"):
        pl_URI = playlist.split("/")[-1]
    elif playlist.startswith("37i"):
        pl_URI = playlist
    else:
        raise ValueError("Unable to access playlist URI")
    return pl_URI


def get_track_info(pl_URI):
    track_uris1 = []
    track_names = []
    artist_uris = []
    artist_names = []
    artist_genre = []
    albums = []
    release_dates = []

    # sound_quality
    acousticness = []
    danceability = []
    energy = []
    instrumentalness = []
    liveness = []
    loudness = []
    speechiness = []
    tempo = []
    valence = []



    playlist = sp.playlist_items(pl_URI)
    for track in playlist["items"]:
        # URI
        track_uri = track["track"]["uri"]
        track_uris1.append(track_uri)

        # Track name
        track_name = track["track"]["name"]
        track_names.append(track_name)

        # Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_uris.append(artist_uri)

        # Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        artist_names.append(artist_name)

        # Genre information
        artist_info = sp.artist(artist_uri)
        artist_genres = artist_info["genres"]
        artist_genre.append(artist_genres)

        # Album
        album = track["track"]["album"]["name"]
        albums.append(album)
        release_day = track["track"]["album"]["release_date"]
        release_dates.append(release_day)

        # Audio features
        audio_info = sp.audio_features(track_uri)[0]
        acousticness.append(audio_info["acousticness"])
        danceability.append(audio_info["danceability"])
        energy.append(audio_info["energy"])
        liveness.append(audio_info["liveness"])
        loudness.append(audio_info["loudness"])
        instrumentalness.append(audio_info["instrumentalness"])
        speechiness.append(audio_info["speechiness"])
        tempo.append(audio_info["tempo"])
        valence.append(audio_info["valence"])


    song_dict = {
        "track_name": track_names,
        "artist_name": artist_names,
        "album": albums,
        "artist_genre": artist_genre,
        "release_date": release_dates,
        "acousticness": acousticness,
        "danceability": danceability,
        "energy": energy,
        "liveness": liveness,
        "loudness": loudness,
        "instrumentalness": instrumentalness,
        "speechiness": speechiness,
        "tempo": tempo,
        "valence": valence,
    }

    ct = datetime.datetime.now()

    song_df = pd.DataFrame(song_dict, columns=["track_name", "artist_name", "album", "artist_genre", "release_date",
                                               "sound_quality"])
    print(song_df, ct)


# get_track_info(TOP_50_GLOBAL_DAILY)
# get_track_info(TOP_50_JP_DAILY)
# print(get_track_info("71d99pLh0TpbdIJESHAsDN"))
