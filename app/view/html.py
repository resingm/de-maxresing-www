import os

from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi import templating
from frontmatter import Frontmatter
from markdown2 import markdown
import requests

import conf

templates = templating.Jinja2Templates(directory=conf.TEMPLATES)

STATUS_MSG = {
    400: ("Bad request", "Sorry, I fear your request cannot be processed by my backend."),
    404: ("Not found", "Sorry, but my backend cannot find the page you are requesting..."),
}

def render_err(req: Request, status_code: int, msg: str):
    name, msg = STATUS_MSG.get(status_code, ("-", None))
    
    context = {
        "status": {
            "code": status_code,
            "name": name,
            "message": msg,
        }
    }
    
    context.update(conf.as_dict())
    return templates.TemplateResponse(
        request=req,
        name="err/base.html.jinja",
        context=context,
    )


def render_page(req: Request, template_name: str, content_name: str, context: dict = None) -> HTMLResponse:
    fpath = os.path.abspath(os.path.join(conf.CONTENT, content_name))
    
    if not fpath.startswith(os.path.abspath(conf.CONTENT) + os.sep):
        return render_err(req, 403, "Access denied.")
    
    if context is None:
        context = { "remote_ip": str(req.client.host) }
    else:
        context.update({"remote_ip": str(req.client.host)})
    
    if not os.path.isfile(fpath):
        # TODO: Implement to return a proper 404 page
        return render_err(req, 404, "Sorry, but my backend cant' find the page you are requesting...")

    # Update context
    # TODO: Reconsider: Do I even need this?
    context.update(conf.as_dict())
    
    # Load content that will be rendered
    fm = Frontmatter.read_file(fpath)
    
    if not fm["attributes"].get("public", False):
        return HTMLResponse(content="Page not found.", status_code=404)
    
    context.update(fm["attributes"])
    
    # Render data in the header first.
    if "content" in context.get("header", { }):
        context["header"]["content"] = markdown(context["header"]["content"])

    # Render remainder of the page
    context["content"] = markdown(fm["body"])
    
    return templates.TemplateResponse(
        request=req,
        name=template_name,
        context=context
    )
    
        
