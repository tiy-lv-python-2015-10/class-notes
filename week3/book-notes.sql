SELECT * FROM books;

SELECT books.isbn, books.title, books.author, books.year, books.id
FROM books;

SELECT *
FROM books
WHERE year = '1997' AND publisher = 'Dell';

SELECT *
FROM ratings
WHERE rating >= 5;

SELECT *
FROM books
WHERE publisher in ('Dell', 'Apple');

SELECT *
FROM books
WHERE publisher = 'Dell' OR publisher = 'Apple';

SELECT *
FROM books
WHERE (publisher = 'Dell' OR publisher = 'Apple') and year = '1997';

SELECT *
FROM books
WHERE publisher like 'Avon%';

SELECT *
FROM books
WHERE lower(publisher) like '%a%';

SELECT *
FROM books
WHERE year > 1997 and year < 2001;

SELECT *
FROM books
WHERE isbn = '0689839049';

SELECT *
FROM ratings
WHERE isbn = '0689839049';


SELECT books.id, books.title, ratings.*
FROM books JOIN ratings ON books.isbn = ratings.isbn
WHERE books.isbn = '0002219980';

SELECT books.id, books.title, ratings.*
FROM books LEFT JOIN ratings ON books.isbn = ratings.isbn
WHERE books.id = 610355;

SELECT *
FROM books
  LEFT JOIN ratings ON books.isbn = ratings.isbn
WHERE year = '1997'
ORDER BY isbn DESC
LIMIT 10;

