import sqlite3
import pandas as pd
import sqlalchemy
from sqlalchemy.engine import cursor

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
conn = sqlite3.connect('my_played_tracks.sqlite')
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


def create_database():
    # Load
    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
    track_name VARCHAR(200),
    artist_name VARCHAR(200),
    album VARCHAR(200),
    release_date VARCHAR(200),
    artist_genres VARCHAR(200),
    timestamp VARCHAR(200),
    CONSTRAINT my_played_tracks PRIMARY KEY (timestamp)
    )
    """
    cursor.execute(sql_query)
    print("Opened database successfully")

    print("Attempting to add data in...")


def update_database():
    # Updating/Appending db into table
    Update_Table = """INSERT OR REPLACE INTO my_played_tracks(track_name, artist_name, album, release_date, 
    artist_genres, timestamp) VALUES(?, ?, ?, ?, ?, ?);"""

    # Taking the values and adding them into the columns
    for track in song_df.values:
        cursor.execute(Update_Table, track)
        conn.commit()
    print("Data successfully adding.")

    conn.close()

    print("Closed database successfully")
