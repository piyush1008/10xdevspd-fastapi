from fastapi import FastAPI, HTTPException,Path
from fastapi.response import JSONResponse
from model.models import User
from model.database import user_collection
from bson import ObjectId
from model.database import post_collection
from model.models import Post
from passlib.context import CryptContext
from utils.utils import verify_password, create_access_token

app = FastAPI()

pwd_context=CryptContext(schemes=["argon2"], deprecated="auto")

# Helper to convert Mongo document
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "email": user["email"]
    }

def post_helper(post)->dict:
    return{
        "id":str(post["_id"]),
        "title":post["title"],
        "content":post["content"],
        "author_id":post["author_id"],
    }

@app.get("/")
async def healthcheck():
    return {"message": "OK"}


#register user
#register user
@app.post("/signup")
async def signup(user: User):
    hashed_password=pwd_context.hash(user.password)
    user_dict=user.dict()
    user_dict['password']=hashed_password
    result=await user_collection.insert_one(user_dict)
    new_user=await user_collection.find_one({"_id":result.inserted_id})
    return user_helper(new_user)

#signin user
@app.post("/signin")
async def signin(user: User):
    user_found=await user_collection.find_one({"username":user.username})
    if not user_found:
        raise HTTPException(status_code=404, detail="User not found")
        
    if not verify_password(user.password, user_found['password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token=create_access_token(data={"id":str(user_found["_id"])})
    # return {"access_token":access_token,"token_type":"bearer"}
    return JSONResponse(content={"access_token":access_token,"token_type":"bearer"}, status_code=200)

# create user
@app.post("/users")
async def create_user(user: User):
    result = await user_collection.insert_one(user.dict())
    print(result)
    new_user = await user_collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

# GET All Users - GET /users/?limit=5&skip=2
@app.get("/users")
async def get_users(limit: int =10, skip: int = 0):
    users = []
    # async for user in user_collection.find():
    #     users.append(user_helper(user))
    # return users
    async for user in user_collection.find().limit(limit).skip(skip):
        users.append(user_helper(user))
    return users

# GET User by ID -- in this we are using path parameter .
@app.get("/users/{id}")
async def get_user(id: str=Path(..., title="ID", description="ID of the user", example="63f1b9b9b9b9b9b9b9b9b9b9") ):
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


@app.get("/post/{id}")
async def get_post(id: str):
    result=await post_collection.find_one({"_id":ObjectId(id)})
    if result:
        return post_helper(result)
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts")
async def create_post(post:Post):
    result=await post_collection.insert_one(post.dict())
    new_post=await post_collection.find_one({"_id":result.inserted_id})
    return post_helper(new_post)