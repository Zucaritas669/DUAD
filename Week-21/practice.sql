# ========================= 1 =====================

Obtenga todos los productos almacenados

# Select *
# from products



# ========================= 2 =====================

Obtenga todos los productos que tengan un precio mayor a 50000

# Select id , name , code ,price 
# from products
# WHERE price > 50000




# ========================= 3 =====================

Obtenga todas las compras de un mismo producto por id.

# SELECT *
# FROM product_invoices
# WHERE product_id = 2;


# ========================= 4 =====================

Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.

# Select product_id, SUM(total_amount)
# From product_invoices
# GROUP BY product_id;


# ========================= 5 =====================

Obtenga todas las facturas realizadas por el mismo comprador


# SELECT user_id ,COUNT (ID), SUM (total_amount)
# FROM invoices
# GROUP BY user_id


# ========================= 7 =====================

Obtenga todas las facturas ordenadas por monto total de forma descendente

# SELECT *
# FROM invoices
# ORDER BY user_id DESC;


# ========================= 8 =====================

Obtenga una sola factura por número de factura.

# SELECT *
# FROM invoices
# GROUP BY invoice_number;




#Extra exercises DB

#============================ 1 ========================

Cree la tabla categories con:

# CREATE TABLE categories(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(25) UNIQUE NOT NULL,
# description TEXT
# );



Agregue a products la columna category_id (INTEGER, puede permitir NULL)

# ALTER TABLE products
# ADD COLUMN category_id INTEGER REFERENCES categories(id);



Actualice algunos products asignándoles un category_id

#UPDATE products SET
#category_id = 1
#WHERE id = 3;

#UPDATE products SET
#category_id = 1
#WHERE id = 1;



 Verifique con SELECT * FROM products (muestre id, product_name, price, category_id, stock_available

# SELECT *
# FROM products;


#id	    code	    name	    price	    entry_date	                brand           stock_available	    category_id
#1	    211965	    GPU	        500.0	    2026-05-15 21:40:29	        ASUS ROCK	    15	                   1
#2	    80327	    Monitor	    85.0	    2026-05-15 21:41:10	        MSI	            25	                   NULL
#3	    276543	    Case	    60000.0	    2026-05-15 23:14:25	        NZXT	        5	                   1



#============================ 2 ========================


Inserte al menos 10 filas en products con product_name, price, stock_available

#INSERT INTO products (code, name, price, brand, stock_available) VALUES
#(1001, 'Laptop Dell Inspiron', 899.99, 'Dell', 15),
#(1002, 'Mouse Logitech MX', 49.99, 'Logitech', 50),
#(1003, 'Teclado Mecánico Redragon', 79.99, 'Redragon', 30),
#(1004, 'Monitor Samsung 24"', 249.99, 'Samsung', 20),
#(1005, 'Auriculares Sony WH-1000', 299.99, 'Sony', 25),
#(1006, 'Webcam Logitech C920', 89.99, 'Logitech', 40),
#(1007, 'Disco SSD Kingston 1TB', 119.99, 'Kingston', 35),
#(1008, 'Memoria RAM Corsair 16GB', 69.99, 'Corsair', 45),
#(1009, 'Silla Gamer DXRacer', 399.99, 'DXRacer', 10),
#(1010, 'Mousepad XL RGB', 29.99, 'Redragon', 60);



Seleccione todos los productos
Seleccione productos con price > 50000

#SELECT *
#FROM products;


#SELECT name, price
#FROM products
#WHERE PRICE > 50000;



Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE

#SELECT name
#FROM products
#WHERE name like 'apple';



Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5

#SELECT name , price
#FROM products
#ORDER BY price DESC;




#============================ 3 ========================


Establezca stock_available = 0 donde price <= 0

#UPDATE product
#SET stock_available = 0 
#WHERE price <= 0 ;



Aumente el price en 100 unidades para todos los productos cuando stock_available sea menor a 10

#UPDATE product
#SET price = price + 100
#WHERE stock_available < 10 ;


Disminuya stock_available en 1 para un product_id específico

#UPDATE products
#SET stock_available = stock_available - 1 
#WHERE id = 13 ;