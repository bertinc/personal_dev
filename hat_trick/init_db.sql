DROP TABLE IF EXISTS people;

CREATE TABLE people (
    pid INTEGER PRIMARY KEY ASC, 
    firstname TEXT,
    lastname TEXT,
    adult INT DEFAULT 1 NOT NULL,
    gender TEXT,
    household_id TEXT DEFAULT 'none' NOT NULL,
    pass INT DEFAULT 0 NOT NULL,
    excludes TEXT DEFAULT ''
);