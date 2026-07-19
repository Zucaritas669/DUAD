import jwt 
from datetime import datetime, timedelta
import os

# Obtener la carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR: {BASE_DIR}")
print(f"Private key path: {os.path.join(BASE_DIR, 'keys', 'private.pem')}")

try:
    with open(os.path.join(BASE_DIR, "keys", "private.pem"), "r") as f:
        PRIVATE_KEY = f.read()
    print("Private key loaded")
except Exception as e:
    print(f"Error loading private key: {e}")
    PRIVATE_KEY = None

try:
    with open(os.path.join(BASE_DIR, "keys", "public.pem"), "r") as f:
        PUBLIC_KEY = f.read()
    print("Public key loaded")
except Exception as e:
    print(f"Error loading public key: {e}")
    PUBLIC_KEY = None

def generate_token(user_id, role):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=15)  # vence en 8 horas
    }
    token = jwt.encode(payload, PRIVATE_KEY , algorithm="RS256")
    return token


def decode_token(token):
    return jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
