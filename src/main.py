import uvicorn, os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.authing_cli import authentication_client

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "NCUT JLCC"}


@app.get("/key")
async def get_current_user(code: str):
    authentication_client.get_access_token_by_code(code)
    
    try:
        with open("./BOX_KEY/KEY", "r") as f:
            key = f.read()
    except FileNotFoundError:
        key = "xxxx"

    return RedirectResponse(url=f"https://ncut-jlcc.top/unlock?key={key}")


if __name__ == "__main__":
    uvicorn.run(app, port=8910)
