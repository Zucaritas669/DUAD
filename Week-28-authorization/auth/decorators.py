from functools import wraps
from flask import request, jsonify
from auth.jwt_handler import decode_token
import jwt

def login_required(f): # Definimos una función que va a ser un decorador y recibe otra función como parámetro

    #Adentro creamos una función decorated que "envuelve" la función original. 
    # *args, **kwargs significa "acepta cualquier parámetro que reciba la función original"
    @wraps(f)
    def decorated(*args, **kwargs):
                    #request.headers.get es un dict con todos los headers que manda el cliente
        auth_header = request.headers.get("Authorization") # Leemos el header Authorization que manda el cliente (ahí va el token). Si no existe, devuelve None.

                                            # startswith método de Python para verificar que el string empieza con ciertas palabras
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify(message="Token missing"), 401
        
        #Sacamos el token (quitamos la palabra "Bearer " al inicio)
        token = auth_header.split(" ")[1]

        try:
            # Verificamos el token con la llave pública
            payload = decode_token(token)

            # Si es válido, guardamos los datos del usuario en request
            request.user = payload

        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expired"), 401
        except jwt.InvalidTokenError:
            return jsonify(message="Invalid token"), 401
        
        return f(*args, **kwargs)
    return decorated


def admin_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        if request.user["role"] != "admin":
            return jsonify(message = "Forbidden: admin access required"),403
        
        return f(*args, **kwargs)
    return decorated