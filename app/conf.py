import os
import dotenv

dotenv.load_dotenv()

# Defaults
BASE_DOMAIN = os.environ.get("MAXRESING_BASE_DOMAIN")
BASE_URL = os.environ.get("MAXRESING_BASE_URL")

# Page configurations
PAGE_NAME = os.environ.get("MAXRESING_PAGE_NAME")

# Landing page
LANDING_PORTRAIT = os.environ.get("MAXRESING_LANDING_PORTRAIT")
LANDING_NAME = os.environ.get("MAXRESING_LANDING_NAME")
LANDING_MAIL = os.environ.get("MAXRESING_LANDING_MAIL")

# Directories
CONTENT = os.environ.get("MAXRESING_DIR_CONTENT", "content")
STATIC = os.environ.get("MAXRESING_DIR_STATIC", "static")
TEMPLATES = os.environ.get("MAXRESING_DIR_TEMPLATES", "templates")

def as_dict():
    
    return {
        "base_url": BASE_URL,
        "page_name": PAGE_NAME,
        "landing": {
            "portrait": LANDING_PORTRAIT,
            "name": LANDING_NAME,
            "mail": LANDING_MAIL,
        },
        "dir": {
            "content": CONTENT,
            "static": STATIC,
            "templates": TEMPLATES,
        }
    }