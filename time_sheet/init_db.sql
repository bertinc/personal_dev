DROP TABLE IF EXISTS entries;

CREATE TABLE entries (
    date TEXT NOT NULL,
    description TEXT,
    start TEXT NOT NULL,
    duration TEXT,
    notes TEXT,
    PRIMARY KEY(date,start)
);