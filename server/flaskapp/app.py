from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
from server.db import db as handler

from tasklist import TaskListApp

app = FastAPI()
templates = Jinja2Templates(directory="templates")

tasklist = TaskListApp()


@app.get('/')
async def index(request: Request):
    tasks = tasklist.index()
    return JSONResponse({"tasks": tasks})
    # return templates.TemplateResponse('index.html', {'request': request, 'tasks': tasks})


@app.post('/add')
async def add_task(request: Request):
    form = request.json()
    tasklist.add_task(form)
    return RedirectResponse('/', status_code=303)


@app.post('/update')
async def update_task(request: Request):
    form = request.json()
    tasklist.update_task(form)
    return RedirectResponse('/', status_code=303)


@app.post('/delete')
async def delete_task(request: Request):
    form = request.json()
    tasklist.delete_task(form)
    return RedirectResponse('/', status_code=303)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
