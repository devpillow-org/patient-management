import jwt

class User:
    def __init__(self,name:str,password:str) -> None:
        self.name = name
        self.password = password
    
    @property
    def payload(self):
        return {
            'user': self.user,
            'password': self.password
        }
    

def get_jwt(user:User):
    payload = {
        "user": user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=900)
    }

    jwt.encode(
        payload=payload,
        algorithm="HS256",
        headers=
    )