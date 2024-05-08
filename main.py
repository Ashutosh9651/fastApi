from fastapi import FastAPI, Path,Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user_by_id(
    id: int = Path(..., description="The ID of the user you want to retrieve", gt=0),
    q:str = Query(None,max_length=5)
    ):
    if len(users) >= id:
        return users[id - 1]
    else:
        return {"message": "User not found"}
