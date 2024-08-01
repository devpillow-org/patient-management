import enum

AUTH_ENCRYPT_KEY = "SECRETKEYEXAMPLE"
TOKEN_EXPIRATION_TIME = 10  # Time in secods for expire token


class AuthHash(enum.StrEnum):
    HS256_ALGORITHM_HASH = "HS256"

    @classmethod
    def available_hashes(cls):
        return [hash for hash in cls]
