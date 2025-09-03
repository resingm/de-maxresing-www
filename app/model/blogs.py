from pathlib import Path

from frontmatter import Frontmatter

def load_blog_listing(blog_dir: Path):
    posts = []
    
    for fpath in sorted(blog_dir.glob("*.md"), reverse=True):
        meta = Frontmatter.read_file(fpath).get("attributes", {})

        if not meta.get("public", False):
            continue
        
        posts.append({
            "title": meta.get("title"),
            "subtitle": meta.get("subtitle"),
            "date": meta.get("date"),
            "header": meta.get("header", {}).get("content"),
            "slug": fpath.stem,
        })

    return posts
            

