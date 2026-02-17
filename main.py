from fastapi import FastAPI, HTTPException
from model.models import User
from model.database import user_collection
from bson import ObjectId

app = FastAPI()

# Helper to convert Mongo document
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "email": user["email"]
    }

@app.get("/")
async def healthcheck():
    return {"message": "OK"}

# CREATE User
@app.post("/users")
async def create_user(user: User):
    result = await user_collection.insert_one(user.dict())
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

# GET All Users
@app.get("/users")
async def get_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# GET User by ID
@app.get("/users/{id}")
async def get_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)
    raise HTTPException(status_code=404, detail="User not found")

# DELETE User
@app.delete("/users/{id}")
async def delete_user(id: str):
    result = await user_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
