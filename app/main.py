import os
import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from frontmatter import Frontmatter
# from markdown2 import markdown

import conf

from api import net
from model import blogs
from view import html

_debug = False
_version = (0, 1, 0)

app = FastAPI(
    debug=_debug,
    version=_version,
)

app.mount("/static", StaticFiles(directory=conf.STATIC), name="static")
app.include_router(net.router, prefix="/api/v1/net")

# templates = Jinja2Templates(directory=conf.TEMPLATES)


@app.get("/")
async def index(req: Request) -> HTMLResponse:

    # Load the blog post listings
    posts = blogs.load_blog_listing(pathlib.Path(os.path.join(conf.CONTENT, "blog")))
    context = {
        "featured": posts[:3],
        "others": posts[3:],
    }
    
    # Simple rendering of the "index.html" page...
    return html.render_page(req, "index.html.jinja", "index.md", context)
    

@app.get("/debug")
async def debug():
    return {
        "configuration": conf.as_dict(),
    }
    
    
@app.get("/{page_id}")
async def page(req: Request, page_id: str) -> HTMLResponse:
    return html.render_page(
        req,
        "page.html.jinja",
        f"{page_id}.md",
    )
    
    
@app.get("/blog/{blog_id}")
async def page(req: Request, blog_id: str) -> HTMLResponse:
    print("blog_id: ", blog_id)
    return html.render_page(
        req,
        "blog.html.jinja",
        f"blog/{blog_id}.md",
    )
    