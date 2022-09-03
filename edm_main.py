import track_extraction
import sqlite3
import sqlalchemy
import spotipy
import Authorization

EDM_PL = "37i9dQZF1DX1kCIzMYtzum"
EDM_HITS = "37i9dQZF1DX3Kdv0IChEm9"
EDM_MIX_JUST_FOR_YOU = "37i9dQZF1EIed8lWkU8WSm"
sp = spotipy.Spotify(client_credentials_manager=Authorization.client_credentials_manager)
DATABASE_LOCATION = "sqlite:///spotify_EDMvsLoFi_new.sqlite"

if __name__ == "__main__":
    # Load
    conn = sqlite3.connect('spotify_EDMvsLoFi_new.sqlite')
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    cursor = conn.cursor()

    # Creating the database if it doesn't exist
    sql_query = """
    CREATE TABLE IF NOT EXISTS EDM_music(
    track_name VARCHAR(200),
    artist_name VARCHAR(200),
    album VARCHAR(200),
    artist_genres VARCHAR(200),
    release_date VARCHAR(200),
    danceability BIT(20),
    energy BIT(20),
    key BIT(20),
    loudness BIT(20),
    mode BIT(20),
    speechiness BIT(20),
    acousticness BIT(20),
    instrumentalness BIT(20),
    liveness BIT(20),
    valence BIT(20),
    tempo BIT(20),
    duration_ms BIT(20),
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name)
    )
    """

    cursor.execute(sql_query)
    print("Opened database successfully")

    # Getting track information
    track_df = track_extraction.fetch_playlist_tracks(sp, "37i9dQZF1DX1kCIzMYtzum")

    # Loading data into database
    print("Attempting to load data into database")

    sql = "INSERT OR REPLACE INTO EDM_music (track_name, artist_name, album, artist_genres, release_date, danceability,"\
          "energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, " \
          "duration_ms) " \
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    # Taking the values and adding them into the columns
    for track in track_df.values:
        print(track)
        cursor.execute(sql, track)
        conn.commit()
    print("Data successfully adding.")
