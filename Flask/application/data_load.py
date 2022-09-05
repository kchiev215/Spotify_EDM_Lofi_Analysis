import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Create a SQL connection to our SQLite database
con = sqlite3.connect("/Users/Thina/Desktop/Spotify_EDM_Lofi_Analysis/spotify_EDMvsLoFi_new"
                      ".sqlite")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
edm_music = cur.execute('SELECT * FROM EDM_music')

for row in cur.execute('SELECT * FROM lofi_music'):
    print(row)


# """Queries"""
# # Return all results of query
# cur.execute('SELECT * FROM my_played_tracks WHERE artist_genres="j-pop"')
# cur.fetchall()
#
# # # Return first result of query
# cur.execute('SELECT * FROM my_played_tracks WHERE artist_genres="j-pop"')
# cur.fetchone()
#
# """Accessing data stored in SQLite using Python and Pandas"""
# # Read sqlite query results into a pandas DataFrame
# df = pd.read_sql_query("SELECT * from my_played_tracks", con)
#
# # Verify that result of SQL query is stored in the dataframe
# print(df.head())
#
# """Storing data: Create new tables using Pandas"""
# # Load the data into a DataFrame
# my_played_tracks = pd.read_sql_query("SELECT * from my_played_tracks", con)
#
# edm = my_played_tracks[my_played_tracks.artist_genres == 'edm']
#
# print(edm)
#
# # Be sure to close the connection
# con.close()
