import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from settings import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "NCUT JLCC"}


@app.get("/key")
async def get_box_key(code: str):
    url = "https://ncut-jlcc.authing.cn/oidc/token"
    payload = {
        "client_id": "6717834b204b7b910e18ffe8",
        "client_secret": settings.authing_client_secret,
        "grant_type": "authorization_code",
        "code": code,
    }

    response = requests.post(url, data=payload)

    # 打印返回的 JSON 数据
    print(response.json())

    # 检查请求是否成功
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "details": response.json()}

    try:
        with open("./ENV/KEY", "r") as f:
            key = f.read()
    except FileNotFoundError:
        key = "xxxx"

    return RedirectResponse(url=f"https://ncut-jlcc.top/unlock?key={key}")


if __name__ == "__main__":
    uvicorn.run(app, port=8910)
