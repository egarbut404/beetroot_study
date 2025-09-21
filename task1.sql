CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

ALTER TABLE books RENAME TO library;

ALTER TABLE library ADD COLUMN year_published INTEGER;

INSERT INTO library (title, author, year_published) VALUES ('Book One', 'Alex', 1995);
INSERT INTO library (title, author, year_published) VALUES ('Book Two', 'John', 2000);
INSERT INTO library (title, author, year_published) VALUES ('Book Three', 'George', 2025);

UPDATE library SET year_published = 2014 WHERE title = 'Book One';

DELETE FROM library WHERE author = 'John';