import redis

class CacheManager():
    def __init__(self, host, port, password , *args, **kwarg):
        self.redis_client = redis.Redis(

            host=host,
            port=port,
            password=password,
            *args, 
            **kwarg
        )
        connection_status = self.redis_client.ping()
        if connection_status:
            print("Connected to redis")
        else:
            print("Could not connect to redis")
    # Crea el cliente de Redis con los datos de conexión 
    # y hace un ping() para confirmar que la conexión realmente sirve.



    def store_data_redis(self, key , value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key,value)
                print("Data saved")

            else:
                self.redis_client.setex(key , time_to_live , value)
        except redis.RedisError as ex:
            print("Error saving data in Redis",ex)
    # Guarda un valor bajo una clave. Si no se pasa time_to_live,
    # el dato queda guardado indefinidamente (set). Si se pasa, 
    # expira solo después de esos segundos (setex).




    def check_key(self, key):
        try:
            key_exist = self.redis_client.exists(key)
            if key_exist:
                ttl = self.redis_client.ttl(key)
                return True, ttl
            return False, None

        except redis.RedisError as ex:
            print(f"An error while checking a key in Redis:",ex)
            return False, None
    # Revisa si una clave existe en Redis. 
    # Devuelve una tupla (existe, ttl_restante), 
    # útil para decidir si vas al cache o a la DB.



    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                return output.decode("utf-8")
            else:
                return None
        except redis.RedisError as ex:
            print(f"An error while retrieving data from Redis:",ex)
    #Obtiene el valor guardado en una clave. Redis devuelve bytes, así que se decodifica a string antes de retornarlo.



    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1
        except redis.RedisError as ex:
            print(f"An error while deleting data from Redis:",ex)
            return False
    # Elimina una clave y su valor. Retorna True si se borró algo,
    # False si la clave no existía (esto es lo que vas a usar para la invalidación de cache).