from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")  


fake_posts_db = [{
    'title': 'First Blog Post',
    'content': 'Content of the first blog post.',
    'author': 'John Doe',
    'publication_date': '2023-06-20',
    'comments': [
        {'author': 'Alice', 'content': 'Great post!'},
        {'author': 'Bob', 'content': 'Intresting read.'}
    ],
    'status': 'published'
},{
    'title': 'Second Blog Post',
    'content': 'Content of the second blog post.',
    'author': 'Jane Smith',
    'publication_date': None,
    'comments': [],
    'status': 'draft'
}]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

    
@app.get("/about")
def about():
    return "All you need to know about Simple Blog"