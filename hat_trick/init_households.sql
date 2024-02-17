--TRUNCATE TABLE IF EXISTS people
-- the exclude column is a pipe delimited list of first names that a person should not get
-- example: 'Easton|Melissa'
-- cols: (pid, firstname, lastname, adult, gender, household_id, pass, excludes)
INSERT INTO people VALUES (NULL, 'Robert', 'Rallison', 1, 'm', 'ral', 0, '');
INSERT INTO people VALUES (NULL, 'Tori', 'Rallison', 1, 'f', 'ral', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Jack', 'Rallison', 1, 'm', 'ral', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Brianna', 'Rallison', 1, 'f', 'ral', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Lori', 'Martin', 1, 'f', 'mar', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Lexy', 'Peterson', 1, 'f', 'pet', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Chris', 'Peterson', 1, 'm', 'pet', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Haden', 'Peterson', 1, 'm', 'pet', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Annie', 'Peterson', 1, 'f', 'pet', 0, 'Easton');
INSERT INTO people VALUES (NULL, 'Easton', 'Peterson', 1, 'm', 'pet', 0, '');
INSERT INTO people VALUES (NULL, 'Melissa', 'Glenn', 1, 'f', 'Glenn', 0, 'Easton');
-- INSERT INTO people VALUES (NULL, 'Natty', 'Saunders', 1, 'f', 'nat', 1, '');
-- INSERT INTO people VALUES (NULL, 'Alex', 'Androes', 1, 'm', 'nat', 1, '');
-- INSERT INTO people VALUES (NULL, 'Milo', 'Androes', 0, 'm', 'nat', 1, '');
-- INSERT INTO people VALUES (NULL, 'Ellie', 'Androes', 0, 'f', 'nat', 1, '');
-- INSERT INTO people VALUES (NULL, 'Tyrel', 'Martin', 1, 'm', 'tyr', 1, '');
-- INSERT INTO people VALUES (NULL, 'Riley', 'Vasquez', 0, 'f', 'tyr', 1, '');
-- INSERT INTO people VALUES (NULL, 'Missy', 'Vasquez', 1, 'f', 'tyr', 1, '');
-- INSERT INTO people VALUES (NULL, 'Ryan', 'Johnson', 1, 'm', 'joh', 1, '');
-- INSERT INTO people VALUES (NULL, 'Sherice', 'Johnson', 1, 'f', 'joh', 1, '');
-- INSERT INTO people VALUES (NULL, 'Louis', 'Johnson', 0, 'm', 'joh', 1, '');
-- INSERT INTO people VALUES (NULL, 'Marley', 'Johnson', 0, 'f', 'joh', 1, '');
-- INSERT INTO people VALUES (NULL, 'Gabby', 'Averatt', 1, 'f', 'ave', 1, '');
-- INSERT INTO people VALUES (NULL, 'Colton', 'Averatt', 1, 'm', 'ave', 1, '');
-- INSERT INTO people VALUES (NULL, 'Elanore', 'Averatt', 0, 'f', 'ave', 1, '');
-- INSERT INTO people VALUES (NULL, 'Emmett', 'Averatt', 0, 'm', 'ave', 1, '');
