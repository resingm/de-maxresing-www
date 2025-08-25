import dotenv
from fastapi import FastAPI

dotenv.load_dotenv()

_debug = False
_version = (0, 1, 0)

app = FastAPI(
    debug=_debug,
    version=_version,
)

@app.get("/")
async def index():
    return {
        "message": "Hello, world!",
    }
