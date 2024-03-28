CREATE TABLE artist (
    id PRIMARY KEY auto_increment NOT NULL,
    fname text NOT NULL, 
    lname text, 
    DOB date NOT NULL
)

CREATE TABLE user (
    id PRIMARY KEY auto_increment NOT NULL,
    username text NOT NULL,
    email text NOT NULL,
    DOC date NOT NULL, 
    password text NOT NULL
)

CREATE TABLE playlist (
    id PRIMARY KEY auto_increment NOT NULL,
    name text NOT NULL,
    DOC date NOT NULL,
    userid int NOT NULL, 
    FOREIGN KEY (userid) REFERENCES user(id)
)

CREATE TABLE songs (
    id PRIMARY KEY auto_increment NOT NULL,
    name text NOT NULL,
    albumid int NOT NULL, 
    FOREIGN KEY (albumid) REFERENCES album(id),
    DOR date NOT NULL,
    genre text NOT NULL,
    length int NOT NULL,
    artistid int NOT NULL,
    FOREIGN KEY (artistid) REFERENCES artist(id)
)

CREATE TABLE album (
    id PRIMARY KEY auto_increment NOT NULL,
    name text NOT NULL, 
    DOC date NOT NULL,
    artistid int NOT NULL, 
    FOREIGN KEY (artistid) REFERENCES artist(id)
)

CREATE TABLE songs_albums(
    albumid int NOT NULL,
    songid int NOT NULL,
    FOREIGN KEY (albumid) REFERENCES album(id),
    FOREIGN KEY (songid) REFERENCES songs(id)
)

CREATE TABLE songs_playlist(
    playlistid int NOT NULL,
    songid int NOT NULL,
    FOREIGN KEY (playlistid) REFERENCES playlist(id),
    FOREIGN KEY (songid) REFERENCES songs(id)
)