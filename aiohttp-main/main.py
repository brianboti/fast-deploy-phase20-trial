"""A small aiohttp service started with `python main.py`, as aiohttp's own quickstart runs it. The application is built
inside main(), so there is no module-level object or factory for a server to import; HOST and PORT come from the
environment, with the quickstart's defaults."""
import os
import platform

import aiohttp
from aiohttp import web


async def index(request):
    return web.json_response({
        "service": "aiohttp-main",
        "trial": "Fast Deploy Phase 20",
        "python": platform.python_version(),
        "aiohttp": aiohttp.__version__,
    })


async def health(request):
    return web.json_response({"ok": True})


def main():
    app = web.Application()
    app.add_routes([web.get("/", index), web.get("/health", health)])
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8080"))
    web.run_app(app, host=host, port=port)


if __name__ == "__main__":
    main()
