
-- =====================
-- Tabla: USERS
-- =====================

SET search_path TO transactions_pgsql;

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
);

-- =====================
-- Tabla: ADDRESSES
-- =====================

CREATE TABLE IF NOT EXISTS addresses(
    id SERIAL PRIMARY KEY,
    address VARCHAR(50) NOT NULL
);

-- =====================
-- Tabla: USER_ADDRESSES
-- =====================

CREATE TABLE IF NOT EXISTS user_addresses(
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);

-- =====================
-- Tabla: PRODUCTS
-- =====================

CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    price INT NOT NULL,
    stock INT NOT NULL,
    note VARCHAR(30) NOT NULL
);

-- =====================
-- Tabla: BILL
-- =====================

CREATE TABLE IF NOT EXISTS bill(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    status VARCHAR(20),

    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================
-- Tabla: BILL_ITEMS
-- =====================

CREATE TABLE IF NOT EXISTS bill_items(
    id SERIAL PRIMARY KEY,
    bill_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity int NOT NULL,

    FOREIGN KEY (bill_id) REFERENCES bill(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);



SET search_path TO transactions_pgsql;

INSERT INTO users (user_name, email) VALUES 
('Shalston', 'shalston@mail.com'),
('Juan', 'juan@mail.com');


INSERT INTO addresses (address) VALUES 
('Nosara, Guanacaste'),
('San José, Costa Rica');


INSERT INTO user_addresses (user_id, address_id) VALUES 
(1, 1),
(2, 2);


INSERT INTO products (name, price, stock, note) VALUES 
('Camisa', 2500, 10, 'Talla M'),
('Zapatos', 8000, 5, 'Talla 42'),
('Pantalón', 4500, 8, 'Talla 32');

