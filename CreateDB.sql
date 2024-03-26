CREATE TABLE artists (
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