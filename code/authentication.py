import datetime
from time import timezone
import jwt



def encode_jwt_token(secret):
    return jwt.encode(
        {"exp": datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(seconds=30)},
        secret,
    )

def decode_jwt_token(jwt_string,secret):
    algorithms = ["HS256"] #TODO: define the correct algorithm to encode this

    try:
        jwt.decode("JWT_STRING", "secret", algorithms=algorithms)
    except jwt.ExpiredSignatureError:
        raise ValueError("The token passed is expired")#TODO: raise correct Exception to fastAPi response