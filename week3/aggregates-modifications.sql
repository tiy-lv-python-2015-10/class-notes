SELECT books.id, books.title, count(*), avg(ratings.rating), min(rating), max(rating)
FROM books
  JOIN ratings on ratings.isbn = books.isbn
GROUP BY books.id, books.title;

SELECT *
FROM books
  JOIN ratings ON ratings.isbn = books.isbn
WHERE books.id = 360195;

select * from ratings limit 10;

SELECT books.id, books.title, count(*) AS rating_count, avg(ratings.rating) AS avg_rating, min(rating), max(rating)
FROM books
  JOIN ratings on ratings.isbn = books.isbn
GROUP BY books.id, books.title
HAVING avg(ratings.rating) > 0 AND count(ratings.rating) > 50
ORDER BY avg(ratings.rating) DESC
LIMIT 10 100;

CREATE DATABASE test;
CREATE INDEX ON ratings (isbn);
CREATE INDEX ON books (isbn);

CREATE TABLE character(
  id SERIAL PRIMARY KEY,
  name varchar(100) NOT NULL,
  age int NOT NULL DEFAULT 0
);

ALTER TABLE public.character ADD page_intro int DEFAULT 0;
ALTER TABLE public.character ALTER COLUMN name TYPE varchar(255);
ALTER TABLE character ADD book_id int NULL;

# 420748
INSERT INTO character (name, age, page_intro, book_id)
    VALUES ('Daffy Duck', 100, 2, 420748), ('Michael Jordan', 52, 1, 420748);

# MAKE SURE TO INCLUDE THE WHERE!!!!!!
UPDATE character
SET name = 'Bugs Bunny',
  age = 50
WHERE id = 1;

SELECT id, title INTO temp_table
FROM books;

SELECT * INTO bttf
FROM books
WHERE year = '1985';
