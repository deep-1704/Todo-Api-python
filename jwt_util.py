import jwt
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv('JWT_SECRET')
def encode_jwt(payload):
    return jwt.encode(payload, secret, algorithm='HS256')

def decode_jwt(token):
    return jwt.decode(token, secret, algorithms=['HS256'])

