import asyncio

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from .models import User


app = FastAPI()


@app.get('/')
async def get():
    return HTMLResponse('')


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    users_count = 0
    await websocket.accept()
    while True:
        await websocket.send_json({'users': int(users_count)})
        await asyncio.sleep(1.)
        user_raw = await websocket.receive_text()
        user = User.parse_raw(user_raw)
        print('Got', user)
        users_count += 1
