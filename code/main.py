from typing import Union

from utils import get_current_timestamp
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "This is the root app my little friends"}


@app.get("/token/generate")
def generate_token():
    token = f"dev-pillow:{get_current_timestamp()}"
    return {"token": token}


@app.get("/token/validate")
def validate_token(item_id: int):
    #TODO: create way to validate if token (that is a timestamp with 'devpillow' flag before) is expired 
    # the toke duration is 10 minutes
    return {"item_id": item_id, "q": q}