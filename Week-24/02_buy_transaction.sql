--Construya una transacción para el proceso de compra de múltiples productos. El bloque debe realizar las siguientes validaciones y acciones:
--Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
--Confirmar que el usuario que realiza la compra existe en la DB.
--Insertar la factura con el usuario relacionado.
--Reducir el stock de los productos según la cantidad comprada





SET search_path TO transactions_pgsql;

DO $$
DECLARE
    v_user_exist INT;
    v_bill_id INT;
    v_stock INT;
    r RECORD;


    v_items INT[][] := ARRAY[[1, 2], [2, 1], [3, 1]];
    i INT;

BEGIN
    Verificar que el usuario existe
    SELECT COUNT(*) INTO v_user_exist
    FROM users
    WHERE id = 1;

    IF v_user_exist = 0 THEN
        RAISE EXCEPTION 'El usuario no existe.';
    END IF;

    Crear la factura
    INSERT INTO bill (user_id, status)
    VALUES (1, 'active')
    RETURNING id INTO v_bill_id;

    -- validar stock e insertar items
    FOR i IN 1..array_length(v_items, 1) LOOP
        DECLARE
            v_product_id INT := v_items[i][1];
            v_quantity   INT := v_items[i][2];
        BEGIN
            -- Validar stock c
            SELECT stock INTO v_stock
            FROM products
            WHERE id = v_product_id;

            IF v_stock IS NULL OR v_stock < v_quantity THEN
                RAISE EXCEPTION 'Stock insuficiente para el producto con id %', v_product_id;
            END IF;

            -- Insertar item en la factura
            INSERT INTO bill_items (bill_id, product_id, quantity)
            VALUES (v_bill_id, v_product_id, v_quantity);

            -- Descontar stock
            UPDATE products
            SET stock = stock - v_quantity
            WHERE id = v_product_id;
        EXCEPTION
            WHEN OTHERS THEN
                -- rollback
                RAISE EXCEPTION 'Error al procesar producto %: %', v_product_id, SQLERRM;
        END;
    END LOOP;

    RAISE NOTICE 'Compra realizada. Factura ID: %', v_bill_id;

END;
$$;


