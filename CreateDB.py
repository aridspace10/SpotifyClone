import sqlite3
conn = sqlite3.connect('Spotify.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fname text NOT NULL, 
    lname text, 
    DOB date NOT NULL
    )''')   

cursor.execute('''CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username text NOT NULL,
    email text NOT NULL,
    DOC date NOT NULL, 
    password text NOT NULL
    )''')

cursor.execute(''' INSERT INTO user (username, email, DOC, password) VALUES
    ('jacko', 'jacko@icloud.com', '2022-12-12', 'jacko123')''')

cursor.execute('''CREATE TABLE playlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name text NOT NULL,
    DOC date NOT NULL,
    userid int NOT NULL, 
    FOREIGN KEY (userid) REFERENCES user(id))
    ''')

cursor.execute(''' INSERT INTO playlist (name, DOC, userid) VALUES
    ('My Playlist', '2022-12-12', 1),
    ('My Playlist 2', '2022-12-12', 1)''')

cursor.execute('''CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name text NOT NULL,
    albumid int NOT NULL, 
    DOR TEXT NOT NULL,
    genre text NOT NULL,
    length int NOT NULL,
    artistid int NOT NULL,
    FOREIGN KEY (artistid) REFERENCES artist(id),
    FOREIGN KEY (albumid) REFERENCES album(id))
    ''')

cursor.execute('''CREATE TABLE album (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name text NOT NULL, 
    DOC date NOT NULL,
    artistid int NOT NULL, 
    FOREIGN KEY (artistid) REFERENCES artist(id))
    ''')  

cursor.execute('''CREATE TABLE songs_albums(
    albumid int NOT NULL,
    songid int NOT NULL,
    FOREIGN KEY (albumid) REFERENCES album(id),
    FOREIGN KEY (songid) REFERENCES songs(id))''')

cursor.execute('''CREATE TABLE songs_playlist(
    playlistid int NOT NULL,
    songid int NOT NULL,
    FOREIGN KEY (playlistid) REFERENCES playlist(id),
    FOREIGN KEY (songid) REFERENCES songs(id)
    )''') 

conn.commit()

conn.close()