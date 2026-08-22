from functools import wraps
from flask import request, jsonify

from Auth.jwt_handler import decode_token
import jwt

def login_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify(message="Token missing"), 401

        token = auth_header.split(" ")[1]

        try:
            
            payload = decode_token(token)
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