import redis

class CacheManager():

    def __init__(self,host,port, password, *args, **kwargs):
        self.redis_client = redis.Redis(
            host = host,
            port = port,
            password = password,
            *args,
            **kwargs
        )
        connection_status = self.redis_client.ping()
        if connection_status:
            print("Connected to redis")
        else:
            print("Could not connect to redis")



    def store_data_redis (self, key, value, time_to_live = None):
        try:
            if time_to_live is None:
                self.redis_client.set(key,value)
                print("Data saved")
            else:
                self.redis_client.setex(key , time_to_live , value)
        except redis.RedisError as ex:
            print("Error saving data in Redis",ex)


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



    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                return output.decode("utf-8")
            else:
                return None
        except redis.RedisError as ex:
            print(f"An error while retrieving data from Redis:",ex)


    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1
        except redis.RedisError as ex:
            print(f"An error while deleting data from Redis:",ex)
            return False