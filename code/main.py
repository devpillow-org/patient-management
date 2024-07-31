from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from utils import get_current_timestamp, has_past_lease

app = FastAPI()

TOKEN_DEFAULT_LEASE = 10  # Token lease time in minutes


@app.get("/")
def read_root():
    return {"Hello": "This is the root app my little friends"}


@app.get("/token/generate")
async def generate_token(response: Response):
    token = f"dev-pillow:{get_current_timestamp()}"
    return {"Authorization": token}


@app.get("/token/validate/{token}")
async def validate_token(request: Request, token: str):
    token_tag, token_timestamp = token.split(":", 2)

    if token_tag != "dev-pillow":
        return JSONResponse(
            content={"authorization": "Ivalid token has submited"}, status_code=400
        )

    if has_past_lease(float(token_timestamp), TOKEN_DEFAULT_LEASE):
        return JSONResponse(
            content={"authorization": "Token lease time is ended"}, status_code=200
        )

    return JSONResponse(content={"token": token}, status_code=200)
