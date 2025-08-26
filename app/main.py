import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import conf

_debug = False
_version = (0, 1, 0)

app = FastAPI(
    debug=_debug,
    version=_version,
)

app.mount("/static", StaticFiles(directory=conf.STATIC), name="static")

templates = Jinja2Templates(directory=conf.TEMPLATES)


@app.get("/")
async def index(req: Request):
    context = {
        "base_url": conf.BASE_URL,
        "page_name": conf.PAGE_NAME,
        "title": "Welcome!",
        "has_header": True,
    }

    return templates.TemplateResponse(
        request=req,
        name="index.html.jinja",
        context=context,
    )
    

@app.get("/debug")
async def debug():
    return {
        "configuration": conf.as_dict(),
    }
    