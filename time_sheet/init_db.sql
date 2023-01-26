DROP TABLE IF EXISTS entries;

CREATE TABLE people (
    eid INTEGER PRIMARY KEY ASC,
    entry_date INT,
    description TEXT,
    start_time TEXT,
    esapsed_time TEXT,
    URL TEXT DEFAULT ''
);