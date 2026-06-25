# health_check.py

from db import PgManager


def health_check():

    db = PgManager(
        db_name="postgres",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    if not db.connection:
        print("DB ERROR. health check")
        return

    tables = ["users", "cars", "rentals"]
    for t in tables:
        result = db.execute_query(
            "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'lyfter_car_rental' AND table_name = %s)", #SELECT 1 , no importa qué selecciona, solo si existe
            t)
        
        if not result[0][0]:
            print(f"DB ERROR. '{t}' does not exist")
            return

    available = db.execute_query("SELECT COUNT(*) FROM lyfter_car_rental.cars WHERE status = 'available'")
    if available[0][0] == 0:
        print("DB ERROR. not cars available")
        return

    print("DB OK.")

    db.close_connection()


health_check()