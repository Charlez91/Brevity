"""
Automated Insertion of bulk posts from json for testing pagination feature.
Warning: There should be at least 2 registered user as the json data contains 2 user. 
"""

import requests
import json
from brevity import create_app, db
from brevity.models import Post, load_user

def scrape_json(url):
    posts = requests.get(url, headers = { "Accept" : "application/json" }).json()
    return posts

def insert_bulk_post(posts):
    app = create_app()
    with app.app_context():
        for p in posts:
            post = Post(title = p.get("title"), content = p.get("content"), author = load_user(p.get("user_id")))
            db.session.add(post)
            db.session.commit()





url = "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json"

posts = scrape_json(url)
insert_bulk_post(posts)
