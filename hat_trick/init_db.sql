DROP TABLE IF EXISTS people;

CREATE TABLE people (
    pid INTEGER PRIMARY KEY ASC, 
    first TEXT,
    last TEXT,
    adult INT DEFAULT 1 NOT NULL,
    gender TEXT,
    household_id TEXT DEFAULT 'none' NOT NULL,
    ignore INT DEFAULT 0 NOT NULL,
    exclude TEXT DEFAULT ''
);

-- the exclude column is a pipe delimited list of first names that a person should not get
-- example: 'Natty|Gabby'
INSERT INTO people VALUES (NULL, 'Robert', 'Rallison', 1, 'm', 'ral', 0, 'Lori');
INSERT INTO people VALUES (NULL, 'Tori', 'Rallison', 1, 'f', 'ral', 0, 'Chris|Lexy');
INSERT INTO people VALUES (NULL, 'Jack', 'Rallison', 0, 'm', 'ral', 0, '');
INSERT INTO people VALUES (NULL, 'Brianna', 'Rallison', 0, 'f', 'ral', 0, '');
INSERT INTO people VALUES (NULL, 'Gabby', 'Averatt', 1, 'f', 'ave', 0, '');
INSERT INTO people VALUES (NULL, 'Colton', 'Averatt', 1, 'm', 'ave', 0, '');
INSERT INTO people VALUES (NULL, 'Elanore', 'Averatt', 0, 'f', 'ave', 1, '');
INSERT INTO people VALUES (NULL, 'Lori', 'Martin', 1, 'f', 'mar', 0, '');
INSERT INTO people VALUES (NULL, 'Lexy', 'Peterson', 1, 'f', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Chris', 'Peterson', 1, 'm', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Haden', 'Peterson', 0, 'm', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Annie', 'Peterson', 0, 'f', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Easton', 'Peterson', 0, 'm', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Natty', 'Saunders', 1, 'f', 'nat', 0, '');
INSERT INTO people VALUES (NULL, 'Alex', 'Androes', 1, 'm', 'nat', 0, '');
INSERT INTO people VALUES (NULL, 'Milo', 'Androes', 0, 'm', 'nat', 0, '');
INSERT INTO people VALUES (NULL, 'Ellie', 'Androes', 0, 'f', 'nat', 0, '');
INSERT INTO people VALUES (NULL, 'Tyrel', 'Martin', 1, 'm', 'tyr', 1, '');
INSERT INTO people VALUES (NULL, 'Riley', 'Vasquez', 0, 'f', 'tyr', 1, '');
INSERT INTO people VALUES (NULL, 'Missy', 'Vasquez', 1, 'f', 'tyr', 1, '');
INSERT INTO people VALUES (NULL, 'Ryan', 'Johnson', 1, 'm', 'joh', 1, '');
INSERT INTO people VALUES (NULL, 'Sherice', 'Johnson', 1, 'f', 'joh', 1, '');
INSERT INTO people VALUES (NULL, 'Louis', 'Johnson', 0, 'm', 'joh', 1, '');
