import os
import dotenv

dotenv.load_dotenv()

# Defaults
BASE_DOMAIN = os.environ.get("MAXRESING_BASE_DOMAIN")
PAGE_NAME = os.environ.get("MAXRESING_BASE_NAME")
BASE_URL = os.environ.get("MAXRESING_BASE_URL")

# Page configurations

# Directories
CONTENT = os.environ.get("MAXRESING_DIR_CONTENT", "content")
STATIC = os.environ.get("MAXRESING_DIR_STATIC", "static")
TEMPLATES = os.environ.get("MAXRESING_DIR_TEMPLATES", "templates")

def as_dict():
    
    return {
        "base_url": BASE_URL,
        "base_name": PAGE_NAME,
        "dir": {
            "content": CONTENT,
            "static": STATIC,
            "templates": TEMPLATES,
        }
    }