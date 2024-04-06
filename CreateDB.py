import sqlite3
conn = sqlite3.connect('SpotifyClone.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fname text NOT NULL, 
    lname text, 
    DOB date
    )''')   

cursor.execute(""" INSERT INTO artist (fname, lname, DOB) VALUES 
    ('Freddie', 'Mercury', '1946-09-05'),
    ('Michael', 'Jackson', '1958-08-29'),
    ('Eagles', NULL, NULL),
    ('Bob', 'Dylan', '1941-05-24'),
    ('Nirvana', NULL, NULL),
    ('Led', 'Zeppelin', NULL),
    ('John', 'Lennon', '1940-10-09'),
    ('The Beatles', NULL, NULL),
    ('Michael', 'Jackson', '1958-08-29'),
    ('Johnny', 'Cash', '1932-02-26'); 
""")

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

cursor.execute(''' INSERT INTO songs (name, albumid, DOR, genre, length, artistid) VALUES 
        ('Bohemian Rhapsody', 1, '1975-10-31', 'Rock', 355, 1),
        ('Thriller', 2, '1982-11-30', 'Pop', 357, 2),
        ('Hotel California', 3, '1976-12-08', 'Rock', 391, 3),
        ('Like a Rolling Stone', 4, '1965-07-20', 'Rock', 371, 4),
        ('Smells Like Teen Spirit', 5, '1991-09-10', 'Grunge', 298, 5),
        ('Stairway to Heaven', 6, '1971-11-08', 'Rock', 482, 6),
        ('Imagine', 7, '1971-09-09', 'Pop', 187, 7),
        ('Hey Jude', 8, '1968-08-26', 'Rock', 431, 8),
        ('Billie Jean', 9, '1982-01-02', 'Pop', 294, 9),
        ('Hurt', 10, '2002-04-17', 'Alternative', 258, 10)
''')

cursor.execute('''CREATE TABLE album (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name text NOT NULL, 
    DOC date NOT NULL,
    artistid int NOT NULL, 
    FOREIGN KEY (artistid) REFERENCES artist(id))
    ''')  

cursor.execute('''INSERT INTO album (name, DOC, artistid) VALUES 
    ('A Night at the Opera', '1975-11-21', 1),
    ('Thriller', '1982-11-30', 2),
    ('Hotel California', '1976-12-08', 3),
    ('Highway 61 Revisited', '1965-08-30', 4),
    ('Nevermind', '1991-09-24', 5),
    ('Led Zeppelin IV', '1971-11-08', 6),
    ('Imagine', '1971-09-09', 7),
    ('The Beatles (White Album)', '1968-11-22', 8),
    ('Thriller', '1982-11-30', 9),
    ('American IV: The Man Comes Around', '2002-11-05', 10);''')

cursor.execute('''CREATE TABLE songs_albums(
    albumid int NOT NULL,
    songid int NOT NULL,
    FOREIGN KEY (albumid) REFERENCES album(id),
    FOREIGN KEY (songid) REFERENCES songs(id))''')

cursor.execute('''CREATE TABLE songs_playlist(
    playlistid int NOT NULL,
    songid int NOT NULL,
    DateAdded text NOT NULL,
    FOREIGN KEY (playlistid) REFERENCES playlist(id),
    FOREIGN KEY (songid) REFERENCES songs(id)
    )''') 

cursor.execute('''INSERT INTO songs_playlist (playlistid, songid, DateAdded) VALUES 
    (1,1, '2024-01-05 22:02:47'),
    (1,2, '2024-03-27 16:45:13'),
    (2,3, '2024-04-05 08:07:23')
''')

conn.commit()

conn.close()