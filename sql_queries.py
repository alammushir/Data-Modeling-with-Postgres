# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays(
	songplay_id SERIAL CONSTRAINT PK_songplays PRIMARY KEY
	, start_time timestamp  REFERENCES time(start_time)
	, user_id int REFERENCES users(user_id)
	, level text
	, song_id text REFERENCES songs(song_id)
	, artist_id text REFERENCES artists(artist_id)
	, session_id int
	, location text
	, user_agent text
    ,CONSTRAINT UQ_start_time_user_id_song_id_artist_id UNIQUE(start_time,user_id,song_id,artist_id)
    )
""")

user_table_create = ("""
CREATE TABLE users(
	user_id int CONSTRAINT PK_users PRIMARY KEY
	, first_name text
	, last_name text
	, gender text
	, level text
	)
""")

song_table_create = ("""
CREATE TABLE songs(
	song_id text CONSTRAINT PK_songs PRIMARY KEY
	, title text
	, artist_id text
	, year int
	, duration numeric(8,5)
    )
""")

artist_table_create = ("""
CREATE TABLE artists(
	artist_id text CONSTRAINT PK_artists PRIMARY KEY
	, name text
	, location text
	, latitude numeric(10,5)
	, longitude numeric(10,5)
	)
""")

time_table_create = ("""
CREATE TABLE time(
	start_time timestamp CONSTRAINT PK_time PRIMARY KEY
	, hour int, day int
	, week int, month int
	, year int
	, weekday int
	)
""")


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES(%s, %s ,%s ,%s ,%s ,%s ,%s ,%s)
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) 
VALUES(%s, %s ,%s ,%s ,%s) ON CONFLICT ON CONSTRAINT pk_users DO 
    UPDATE SET  level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) 
VALUES(%s, %s ,%s ,%s ,%s) ON CONFLICT ON CONSTRAINT pk_songs DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude , longitude) 
VALUES(%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT pk_artists DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT pk_time DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT 
	s.song_id
	, s.artist_id 
FROM songs s 
INNER JOIN artists a 
	ON a.artist_id = s.artist_id 
WHERE s.title = %s 
	AND a.name = %s 
	AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]