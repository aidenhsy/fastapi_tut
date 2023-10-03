from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        middle_name="A",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student],
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        middle_name="B",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


@app.get("/")
async def root():
    return {"Hello": "Aiden"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exist"
    )
