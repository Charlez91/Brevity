"""
Automated Insertion of bulk posts from json for testing pagination feature.
"""


import requests
import json
from brevity import db
from brevity.models import Post, load_user

url = "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json"

posts = requests.get(url, headers = { "Accept" : "application/json" }).json()

for p in posts:
    post = Post(title = p.get("title"), content = p.get("content"), author = load_user(p.get("user_id")))
    db.session.add(post)
    db.session.commit()


