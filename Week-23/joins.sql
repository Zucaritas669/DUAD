Obtenga todos los libros y sus autores (en caso de tenerlos)

SELECT books.name AS B, authors.name AS A
FROM books
LEFT JOIN authors ON books.author_id = authors.id;

+-------------------------+---------------------+
|   B                     |     A               |
+-------------------------+---------------------+
| Don Quijote             | Miguel de Cervantes |
| La Divina Comedia       | Dante Alighieri     |
| Vagabond 1-3            | Takehiko Inoue      |
| Dragon Ball 1           | Akira Toriyama      |
| The Book of the 5 Rings | NULL                |
+-------------------------+---------------------+




Obtenga todos los libros que no tienen autor

SELECT books.name AS B, authors.name AS A
FROM books
LEFT JOIN authors ON books.author_id = authors.id
WHERE books.author_id IS NULL;

+-------------------------+------+
| libro                   | autor|
+-------------------------+------+
| The Book of the 5 Rings | NULL |
+-------------------------+------+


Obtenga todos los autores que no tienen libros

SELECT authors.name as Author
From authors
LEFT JOIN books ON books.author_id = authors.id
WHERE books.author_id IS NULL;

+-------------+
| Author      |
+-------------+
| Walt Disney |
+-------------+


Obtenga todos los libros que han sido rentados en algún momento

SELECT rents.book_id as Book, rents.state as State 
from rents
INNER JOIN books ON books.id = rents.book_id

+------+----------+
| Book | State    |
+------+----------+
| 1    | Returned |
| 2    | Returned |
| 1    | On time  |
| 3    | On time  |
| 2    | Overdue  |
+------+----------+


Obtenga todos los libros que nunca han sido rentados

SELECT rents.book_id as Book, books.name as Name, rents.state as State 
from books
LEFT JOIN rents ON books.id = rents.book_id
WHERE state IS NULL

+------+-------------------------+-------+
| Book | Name                    | State |
+------+-------------------------+-------+
| NULL | Dragon Ball 1           | NULL  |
| NULL | The Book of the 5 Rings | NULL  |
+------+-------------------------+-------+



Obtenga todos los clientes que nunca han rentado un libro

SELECT customers.id AS ID, customers.name AS Name
FROM customers
LEFT JOIN rents ON customers.id = rents.customer_id
WHERE rents.customer_id is NULL


+----+----------------+
| ID | Name           |
+----+----------------+
| 3  | Luke Skywalker |
+----+----------------+


Obtenga todos los libros que han sido rentados y están en estado “Overdue”

SELECT books.name as Book, customers.name as Renter, rents.state as State
from books
INNER JOIN rents ON books.id = rents.book_id
INNER JOIN customers ON rents.customer_id = customers.id
WHERE rents.state = 'Overdue'

+------------------+----------+---------+
| Book             | Renter   | State   |
+------------------+----------+---------+
| La Divina Comedia| Jane Doe | Overdue |
+------------------+----------+---------+




1. Explicación cruzada entre conjuntos y SQL
Analice la operación de conjuntos All - Odd.
Explique cómo una operación similar se puede representar en SQL con JOINs.
¿Qué tipo de JOIN usaría?



All -   Odd significa: tomar todos los elementos de All y quitar los que aparecen en Odd 

En SQL se representa con LEFT JOIN porque queremos todos los de All aunque no tengan pareja en Odd

El WHERE Odd.numero IS NULL filtra solo los que no tuvieron pareja, es decir, los que no estaban en Odd

El resultado sería {2,4,6,8,10}



Agrupamiento y conteo cruzado
Usando las tablas de Books, Customers y Rents:

Obtenga el número total de veces que cada cliente ha rentado un libro

SELECT COUNT(customers.id) AS Count, customers.name as NAME, books.name AS Books
from customers
INNER JOIN rents ON customers.id = rents.customer_id
INNER JOIN books ON rents.book_id = books.id
GROUP BY customers.name


Ordene de mayor a menor y limite el resultado a los 3 clientes más activos

SELECT COUNT(customers.id) AS has_rented, customers.name AS name
fROM customers 
INNER JOIN rents ON customers.id = rents.customer_id
GROUP BY customers.name
ORDER BY has_rented DESC 
LIMIT 3


3. Consulta con múltiples JOINS anidados
Genere un SELECT que devuelva lo siguiente:
Nombre del cliente
Nombre del libro
Nombre del autor
Estado del alquiler (Rents.State)
Debe manejar el caso en que un libro no tenga autor


SELECT customers.name AS CUSTOMER_NAME, books.name AS BOOK_NAME, 
authors.name AS AUTHOR_NAME, rents.state AS STATUS
FROM rents
INNER JOIN customers ON rents.customer_id = customers.id
INNER JOIN books on rents.book_id = books.id
LEFT JOIN authors ON books.author_id = authors.id
