DROP TABLE IF EXISTS rt_categories;

CREAT TABLE rt_categories (
    category VARCHAR(15) NOT NULL,
    description TEXT,
    PRMARY KEY(category)
);

INSERT INTO rt_categories (category, description)
VALUES
('DEV', 'application and database development'),
('FILM', 'film production or research and development'),
('IMAGING', 'anything to do with image process development or production work'),
('IT', 'administration of computer hardware or sofware services'),
('WET', 'wet processing development or production work'),
('SETUP', 'any time spent physicall setting up a work space or environment'),
('MISC', 'stuff that cannot or does not need to be categorized'),
('COLAB', 'planning, administrative, brainstorming, and team building');

DROP TABLE IF EXISTS dt_entries;

CREATE TABLE dt_entries (
    date TEXT NOT NULL,
    description TEXT,
    start TEXT NOT NULL,
    duration TEXT,
    notes TEXT,
    category TEXT,
    PRIMARY KEY(date,start)
    FOREIGN KEY (category) REFERENCES rt_categories(category)
);