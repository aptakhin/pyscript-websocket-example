# pyscript-websocket-example

Just tiny PyScript websocket example Pydantic and server.

PyScript doesn't require installation right now, it uses latest web bundle.

For local usage ports `8000` and `8001` are used.

For server side:

```bash
poetry install
poetry run uvicorn www.server:app
```

```bash
python3 -m http.server 8001
```

Now open: http://localhost:8001/www/pydantic.html

![browser screen](docs/browser.jpg)
