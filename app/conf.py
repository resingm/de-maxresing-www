import os
import dotenv

dotenv.load_dotenv()

# Defaults
BASE_URL = os.environ.get("MAXRESING_BASE_URL")

# Page configurations
PAGE_NAME = os.environ.get("MAXRESING_PAGE_NAME")

# Directories
CONTENT = os.environ.get("MAXRESING_DIR_CONTENT", "content")
STATIC = os.environ.get("MAXRESING_DIR_STATIC", "static")
TEMPLATES = os.environ.get("MAXRESING_DIR_TEMPLATES", "templates")

def as_dict():
    
    return {
        "base_url": BASE_URL,
        "page_name": PAGE_NAME,
        "directories": {
            "content": CONTENT,
            "static": STATIC,
            "templates": TEMPLATES,
        }
    }