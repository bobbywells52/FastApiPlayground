from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
import models
from Database import engine, SessionLocal
from models import ToDos
from pydantic import BaseModel, Field
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency =Annotated[ Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str
    priority: int = Field(gt=0)
    complete: bool

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(ToDos).all()

@app.get("/todo/{todo_id}", status_code=200)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(ToDos).filter(ToDos.id == todo_id).first()

    if  todo_model is not None:
        return todo_model

    raise HTTPException(status_code=404, detail= 'ToDo not found')

@app.post("/todo", status_code=201)
async def create_todo(db: db_dependency, todo_request: TodoRequest):

    todo_model = ToDos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()

@app.put("/todo/{todo_id}", status_code=204)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    todo_model= db.query(ToDos).filter(ToDos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='ToDo not found')

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}", status_code=204)
async def delete_todo(db:db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(ToDos).filter(ToDos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='ToDo not found')

    db.delete(todo_model)
    db.commit()

