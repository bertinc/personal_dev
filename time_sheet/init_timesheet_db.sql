DROP TABLE IF EXISTS rt_category;

CREATE TABLE rt_category (
    category VARCHAR(15) NOT NULL,
    description TEXT,
    PRIMARY KEY(category)
);

INSERT INTO rt_category (category, description)
VALUES
('DEV', 'application and database development'),
('FILM', 'film production or research and development'),
('IMAGING', 'anything to do with image process development or production work'),
('IT', 'administration of computer hardware or sofware services'),
('WET', 'wet processing development or production work'),
('SETUP', 'any time spent physicall setting up a work space or environment'),
('MISC', 'stuff that cannot or does not need to be categorized'),
('COLAB', 'planning, administrative, brainstorming, and team building'),
('NONE', 'instead of erroring out, we will use this when an invalid category is entered');

DROP TABLE IF EXISTS dt_entry;

CREATE TABLE dt_entry (
    date TEXT NOT NULL,
    description TEXT,
    start TEXT NOT NULL,
    duration TEXT,
    notes TEXT,
    category TEXT NOT NULL,
    PRIMARY KEY(date,start),
    FOREIGN KEY (category) REFERENCES rt_category(category)
);