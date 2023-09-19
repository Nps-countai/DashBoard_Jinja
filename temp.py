import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import pandas as pd
from datetime import datetime, timedelta
import time
from dataLoader import updatedData

templates = Jinja2Templates(directory="templates") 

# last hr time
last_hour_date_time = datetime.now() - timedelta(hours = 1)
lh_time = last_hour_date_time.strftime('%Y-%m-%d %H:%M:%S')

# app starting
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# about page rendering
@app.get("/about")
async def about():
    return "Need to link data"

# index page rendering
@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, 
                                                    "mills" : pd.read_csv('new.csv'),
                                                    "lh_time" : lh_time})

def runApp():
    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8088)
    
