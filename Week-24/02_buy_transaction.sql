--Construya una transacción para el proceso de compra de múltiples productos. El bloque debe realizar las siguientes validaciones y acciones:
--Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
--Confirmar que el usuario que realiza la compra existe en la DB.
--Insertar la factura con el usuario relacionado.
--Reducir el stock de los productos según la cantidad comprada





DO  $$
DECLARE 
    v_stock INT;
    v_user_exist INT;
    v_bill_id INT ;

BEGIN
    SELECT COUNT(*) INTO v_user_exist
    FROM users
    WHERE id = 1;

    IF v_user_exist = 0 THEN
        RAISE EXCEPTION 'El usuario no existe.';
    END IF;


    SELECT stock INTO v_stock
    FROM products
    WHERE id = 1;

    IF v_stock IS NULL OR v_stock < 1 THEN
        RAISE EXCEPTION 'Stock insuficiente';
    END IF;

    SELECT stock INTO v_stock
    FROM products
    WHERE id = 2;

    IF v_stock IS NULL OR v_stock < 1 THEN
        RAISE EXCEPTION 'Stock insuficiente';
    END IF;


    SELECT stock INTO v_stock
    FROM products
    WHERE id = 3;

    IF v_stock IS NULL OR v_stock < 1 THEN
        RAISE EXCEPTION 'Stock insuficiente';
    END IF;

    INSERT INTO bill (user_id, status)
    VALUES (1, 'active')
    RETURNING id INTO v_bill_id;

    BEGIN
        INSERT INTO bill_items (bill_id, product_id, quantity)
        VALUES (v_bill_id, 1, 2),
                (v_bill_id, 2, 1);

        UPDATE products SET stock = stock - 2 WHERE id = 1;
        UPDATE products SET stock = stock - 1 WHERE id = 2;

        RAISE NOTICE 'Compra realizada. Factura ID: %', v_bill_id;
    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Error al procesar items: ', v_bill_id;
    END;

END;
$$;


