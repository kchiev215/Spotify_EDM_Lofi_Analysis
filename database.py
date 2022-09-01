import sqlite3
import pandas as pd
import sqlalchemy
import mysql.connector
import Authorization

# DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
# conn = sqlite3.connect('my_played_tracks.sqlite')
# engine = sqlalchemy.create_engine(DATABASE_LOCATION)
# cursor = conn.cursor()

conn = mysql.connector.connect(
    host="localhost",
    user=Authorization.my_sql_username,
    password=Authorization.my_sql_password,
    database="spotify_comparison"
)


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


def create_load_lofi():
    # Load
    sql_query = """
    CREATE TABLE IF NOT EXISTS lofi_music(
    track_name VARCHAR(200),
    artist_name VARCHAR(200),
    album VARCHAR(200),
    release_date VARCHAR(200),
    artist_genres VARCHAR(200),
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name)
    )
    """
    cursor = conn.cursor()

    cursor.execute(sql_query)

    print("Opened database successfully")

    Update_Table = """INSERT OR REPLACE INTO lofi_music(track_name, artist_name, album, release_date, 
    artist_genres) VALUES(?, ?, ?, ?, ?, ?);"""

    conn.close()


def create_load_EDM():
    # Load
    sql_query = """
    CREATE TABLE IF NOT EXISTS EDM_music(
    track_name VARCHAR(200),
    artist_name VARCHAR(200),
    album VARCHAR(200),
    release_date VARCHAR(200),
    artist_genres VARCHAR(200),
    CONSTRAINT track_info PRIMARY KEY (track_name, artist_name)
    )
    """
    cursor = conn.cursor()

    cursor.execute(sql_query)

    print("Opened database successfully")

    conn.close()
