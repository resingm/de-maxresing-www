import random
import ipaddress

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse

from model import net

MAX_REQ_N = 100000

router = APIRouter()


@router.get("/ip/", tags=["net"])
async def get_ip(req: Request) -> PlainTextResponse:
    remote_ip, _ = req.client
    return PlainTextResponse(remote_ip)


@router.get("/ipv4/random", tags=["net", "ipv4"])
async def get_random_ipv4(req: Request, n: int = 1) -> PlainTextResponse:
    if n > MAX_REQ_N:
        return PlainTextResponse("Cannot request more than 100,000 IPv4s at a time.", status_code=400)
    
    arr = net.get_random_ipv4(n)
    return PlainTextResponse("\n".join(arr))

@router.get("/ipv6/random", tags=["net", "ipv6"])
async def get_random_ipv6(req: Request, n: int = 1) -> PlainTextResponse:
    if n > MAX_REQ_N:
        return PlainTextResponse("Cannot request more than 100,000 IPv6s at a time.", status_code=400)
    
    arr = net.get_random_ipv6(n)
    return PlainTextResponse("\n".join(arr))
    