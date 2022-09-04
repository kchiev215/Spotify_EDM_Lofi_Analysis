"""TRACK INFORMATION NEEDED FOR ANALYSIS"""
import spotipy
import pandas as pd
import datetime
import Authorization

sp = spotipy.Spotify(client_credentials_manager=Authorization.client_credentials_manager)


def get_spotify_featured_URI(playlist):
    if playlist.startswith("https://api.spotify.com/v1/playlists/") | playlist.startswith(
            "https://open.spotify.com/playlist/"):
        pl_URI = playlist.split("/")[-1]
    elif playlist.startswith("37i"):
        pl_URI = playlist
    else:
        raise ValueError("Unable to access playlist URI")
    return pl_URI


def fetch_playlist_tracks(sp, playlistsid):
    offset = 0
    tracks = []
    # Make the API request
    while True:
        content = sp.playlist_tracks(playlistsid, fields=None, limit=100, offset=offset, market=None)
        tracks += content['items']

        if content['next'] is not None:
            offset += 100
        else:
            break

    track_uris1 = []
    track_names = []
    artist_uris = []
    artist_names = []
    artist_genre = []
    albums = []
    release_dates = []
    track_ids = []

    # sound features
    audio_infos = []
    danceability = []
    energy = []
    key = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    duration_ms = []

    for track in tracks:
        if track["track"] is not None:

            # Track ID
            track_id = track["track"]["id"]
            track_ids.append(track_id)

            # Track name
            track_name = track["track"]["name"]
            track_names.append(track_name)

            # Main Artist Information (Name)
            artist_name = track["track"]["artists"][0]["name"]
            artist_names.append(artist_name)

            # Artist Genre information
            artist_uri = track["track"]["artists"][0]["uri"]
            artist_info = sp.artist(artist_uri)

            # Appending genres as a single item as list does not append well into DB
            artist_genres = artist_info["genres"]
            if len(artist_genres) == 0:
                artist_genre.append("Not available")
            else:
                artist_genre.append(artist_genres[0])

            # Album Information (album name and release date)
            album = track["track"]["album"]["name"]
            albums.append(album)
            release_day = track["track"]["album"]["release_date"]
            release_dates.append(release_day)

        else:
            track_uris1.append("None")
            track_ids.append("None")
            track_names.append("None")
            artist_uris.append("None")
            artist_names.append("None")
            artist_genre.append("None")
            albums.append("None")
            release_dates.append("None")

    # NoneType filter
    for track_ID in track_ids:
        audio_info = sp.audio_features(track_ID)[0]  # Get audio features for this specific track
        if audio_info != None:
            audio_infos.append(audio_info)
        else:
            keys = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
            value = "None"
            audio_info = {i: value for i in keys}
            audio_infos.append(audio_info)

    # Audio features
    for audio_info in audio_infos:
        danceability.append(audio_info["danceability"])
        energy.append(audio_info["energy"])
        key.append(audio_info["key"])
        loudness.append(audio_info["loudness"])
        mode.append(audio_info["mode"])
        speechiness.append(audio_info["speechiness"])
        acousticness.append(audio_info["acousticness"])
        instrumentalness.append(audio_info["instrumentalness"])
        liveness.append(audio_info["liveness"])
        valence.append(audio_info["valence"])
        tempo.append(audio_info["tempo"])
        duration_ms.append(audio_info["duration_ms"])

    song_dict = {
        "track_name": track_names,
        "artist_name": artist_names,
        "album": albums,
        "artist_genre": artist_genre,
        "release_date": release_dates,
        "danceability": danceability,
        "energy": energy,
        "key": key,
        "loudness": loudness,
        "mode": mode,
        "speechiness": speechiness,
        "acousticness": acousticness,
        "instrumentalness": instrumentalness,
        "liveness": liveness,
        "valence": valence,
        "tempo": tempo,
        "duration_ms": duration_ms,
    }

    ct = datetime.datetime.now()

    song_df = pd.DataFrame(song_dict, columns=song_dict.keys())
    return song_df
