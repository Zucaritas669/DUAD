SET search_path TO transactions_pgsql;


DO $$
DECLARE
    v_bill_exists INT;
    r RECORD;

BEGIN
    -- Verificar que la factura existe
    SELECT COUNT(*) INTO v_bill_exists
    FROM bill
    WHERE id = 1;

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'La factura no existe.';
    END IF;

    -- Restaurar el stock 
    FOR r IN
        SELECT product_id, quantity
        FROM bill_items
        WHERE bill_id = 1
    LOOP
        UPDATE products
        SET stock = stock + r.quantity
        WHERE id = r.product_id;
    END LOOP;

    --  Marcar la factura como retornada
    UPDATE bill
    SET status = 'Retornada'
    WHERE id = 1;

    RAISE NOTICE 'Devolución procesada correctamente.';

END;
$$;




