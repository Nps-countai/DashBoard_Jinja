from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import pandas as pd
from datetime import datetime, timedelta
last_hour_date_time = datetime.now() - timedelta(hours = 1)
lh_time = last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')

templates = Jinja2Templates(directory="templates")  
df = pd.read_csv('new.csv')


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/about")
def about():
    return "All you need to know about Simple Blog"

@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, 
                                                    "mills" : df,
                                                    "lh_time" : lh_time})