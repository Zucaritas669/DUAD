from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

# Calcula la raíz del proyecto sin importar desde dónde se ejecute
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS_DIR = os.path.join(BASE_DIR, "keys")
os.makedirs(KEYS_DIR, exist_ok=True)

# Generar la llave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Generar la llave pública a partir de la privada
public_key = private_key.public_key()

# Guardar la llave privada
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open(os.path.join(KEYS_DIR, "private.pem"), 'wb') as f:
    f.write(private_pem)

# Guardar la llave pública
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open(os.path.join(KEYS_DIR, "public.pem"), 'wb') as f:
    f.write(public_pem)

print("Llaves generadas exitosamente")