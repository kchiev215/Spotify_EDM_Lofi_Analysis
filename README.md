# Audio Analysis of EDM and Lofi Music on Spotify

Used Spotify's API to retrieve the audio features of Lofi and EDM tracks on Spotify for a in-depth analysis of attributes which makes them different from one another.

### Inspiration behind the analysis:
- **Lofi**: Typically seen to be used to de-stress at the end of the day or studying needs
- **EDM**: Uplifting one's mood, rave festivals/concerts, jamming out
- **Curiousity**: What attributes best fits each music type and how does it link to the activities others use them for in their daily lives

### Tools used:
Back-end: 

- Pycharm
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- SQLite Database

Front-end Creation:

- Flask
- Boot
- HTML/CSS

### Method:
1. Developed a pipeline to retrieve metadata from API:
	- Track title
	- Release title
	- Artist name
	- Artist_genre
	- Release Date
	- Audio features:
		- Danceability
		- Energy
		- Key
		- Loudness
		- Mode
		- Speechiness
		- Acousticness
		- Instrumentalness
		- Liveness
		- Valence
		- Tempo
		- Duration(ms)
	- For a more in-depth description of the audio features, refer back to this [link](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features) 
2. Uploaded the data into a SQLite database 
	- The tracks obtained and loaded into the database were from Spotify featured playlists and split into 2 different tables based on their genre for analysis
3. Uploaded SQLite database into Jupyter Notebook for analysis:
	- Correlations
	- Audio features vs frequency
		- Used to determine which audio features are prominant in each genre
4. Created front-end on Flask using Python and bootstrap for presentation
5. Wrote up conclusions based off of findings from analysis


### Discussion:
- Spotify tracks do not include track genre:
	- However, there are artist genres which may not be accurate to the track itself as artists likes to try new techniques and skills which could place their song in a genre different than their own.
		- Could be an idea to add genre to assist with their ML/recommendations, if not already used for recomending music

### Conclusion:
- TDB