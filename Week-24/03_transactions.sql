SET search_path TO transactions_pgsql;

DO $$
DECLARE
    v_bill_exists INT;

BEGIN
    
    SELECT COUNT(*) INTO v_bill_exists
    FROM bill
    WHERE id = 1;

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'La factura no existe.';
    END IF;

    
    UPDATE products SET stock = stock + 2 WHERE id = 1;
    UPDATE products SET stock = stock + 1 WHERE id = 2;

    UPDATE bill SET status = 'Retornada' WHERE id = 1;

    RAISE NOTICE 'Devolución procesada correctamente.';

END;
$$;




