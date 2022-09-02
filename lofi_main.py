import track_extraction
import database
import sqlite3
import pandas as pd
import sqlalchemy

LOFI_BEATS = "37i9dQZF1DWWQRwui0ExPn"

DATABASE_LOCATION = "sqlite:///spotify_EDMvsLoFi.sqlite"

if __name__ == "__main__":
    # Load
    conn = sqlite3.connect('spotify_EDMvsLoFi.sqlite')
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    cursor = conn.cursor()

    # Creating db if not made
    sql_query = """
    CREATE TABLE IF NOT EXISTS lofi_music(
    track_name VARCHAR(200),
    artist_name VARCHAR(200),
    album VARCHAR(200),
    release_date VARCHAR(200),
    artist_genres VARCHAR(200),
    acousticness VARCHAR(20),
    danceability VARCHAR(20),
    energy VARCHAR(20),
    liveness VARCHAR(20),
    loudness VARCHAR(20),
    instrumentalness VARCHAR(20),
    speechiness VARCHAR(20),
    tempo VARCHAR(20),
    valence VARCHAR(20),
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name)
    )
    """
    cursor.execute(sql_query)
    print("Opened database successfully")

    # Getting track information
    track_df = track_extraction.get_track_info("37i9dQZF1DWWQRwui0ExPn")

    # Loading data into database
    print("Attempting to load data into database")

    sql = "INSERT OR REPLACE INTO lofi_music (track_name, artist_name, album, release_date, artist_genres, " \
          "acousticness, " \
          "danceability, energy, liveness, loudness, instrumentalness, speechiness, tempo, valence) " \
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    # Taking the values and adding them into the columns
    for track in track_df.values:
        print(track)
        cursor.execute(sql, track)
        conn.commit()
    print("Data successfully adding.")
