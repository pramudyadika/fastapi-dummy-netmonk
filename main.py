from fastapi import FastAPI
from model import PostSchema

posts = [
    {
        "id": 1,
        "title": "some title",
        "content": "some content"
    },
    {
        "id": 2,
        "title": "another title",
        "content": "another content"
    },
    {
        "id": 3,
        "title": "yet another title",
        "content": "yet another content"
    }

]

users = []

app = FastAPI()

# Get for testing
@app.get("/", tags=["Test"])
async def greet():
    return {"Hello": "World"}

# Get all posts
@app.get("/posts", tags=["Posts"])
async def get_posts():
    return {"data": posts}

# Get a single post
@app.get("/posts/{id}", tags=["Posts"])
async def get_one_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {"data": post}
    return {"error": "Post not found"}