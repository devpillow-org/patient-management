import datetime
from typing import Any, Dict, Union

import jwt
from constants import AUTH_ENCRYPT_KEY, TOKEN_EXPIRATION_TIME, AuthHash


class AuthBackend:
    encrypt_key = AUTH_ENCRYPT_KEY
    default_hash = AuthHash.HS256_ALGORITHM_HASH

    @classmethod
    def _encode_hs256(cls, payload: Dict[str, Any]):
        encoded = jwt.encode(
            payload=payload,
            key=cls.encrypt_key,
            algorithm=cls.default_hash.value,
        )
        return encoded

    @classmethod
    def make_password(cls, raw_password: str) -> bool:
        payload = {"password": raw_password}
        encoded = cls.encode(payload)
        return encoded

    @classmethod
    def check_password(cls, raw_password: str, token: str) -> bool:
        payload = cls.encode({"password": raw_password})
        return token == payload

    @classmethod
    def get_auth_token(cls) -> str:
        now = datetime.datetime.now().timestamp()
        payload = {"authorization": f"{str(now)}"}
        return cls.encode(payload)

    @classmethod
    def check_token_lease(cls, token: Union[str, float]) -> Dict:
        now = datetime.datetime.now()
        token_created_time = datetime.datetime.fromtimestamp(token)
        difference_time = now - token_created_time
        is_expired = difference_time >= datetime.timedelta(
            seconds=TOKEN_EXPIRATION_TIME,
        )

        return (
            {"authorization": "Submitted token expired"}
            if is_expired is True
            else {"authorization": token}
        )

    @classmethod
    def encode(cls, payload: Dict[str, Any], hash: Union[str, None] = None):
        if hash is None:
            hash = cls.default_hash

        if hash == cls.default_hash:
            return cls._encode_hs256(payload)

        try:
            hash = AuthHash(hash)
            # TODO: IMPLEMENT METHODS TO ENCONDE OTHERS HASHES
        except ValueError as err:
            raise ValueError(err)


if __name__ == "__main__":
    password = "devpillow"
    encoded = AuthBackend.make_password(password)
    is_valid = AuthBackend.check_password(password, encoded)
    print(is_valid)
