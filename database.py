import sqlite3
import pandas as pd
import sqlalchemy
import mysql.connector
import Authorization
import track_extraction

DATABASE_LOCATION = "sqlite:///spotify_EDMvsLoFi.sqlite"
conn = sqlite3.connect('spotify_EDMvsLoFi.sqlite')
engine = sqlalchemy.create_engine(DATABASE_LOCATION)
cursor = conn.cursor()


# Validate data
def validate_songs_data(df: pd.DataFrame):
    # Empty Dataset check
    if df.empty:
        print("The recently played song list is empty. Exiting execution.")
        return False

    # Primary key check
    if pd.Series(df["timestamp"]).is_unique:
        pass
    else:
        raise Exception("Primary Key constraint violated.")

    # Null check
    if df.isnull().values.any():
        raise Exception("Null values are present in the dataset. Exiting execution.")


def create_load_LoFi():
    # Load
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
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name),
    )
    """
    cursor.execute(sql_query)


def create_load_EDM():
    sql_query = """
    CREATE TABLE IF NOT EXISTS EDM_music(
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
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name),
    )
    """

    cursor.execute(sql_query)


def insert_data_Lofi(track_df):
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


def insert_data_EDM(track_df):
    sql = "INSERT OR REPLACE INTO lofi_music (track_name, artist_name, album, release_date, artist_genres, " \
          "acousticness, " \
          "danceability, energy, liveness, loudness, instrumentalness, speechiness, tempo, valence) " \
          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?"

    # Taking the values and adding them into the columns
    for track in track_df.values:
        print(track)
        cursor.execute(sql, track)
        conn.commit()
    print("Data successfully adding.")
