from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL="mongodb+srv://piyushsunny:piyushsunny@cluster0.lxzr5mx.mongodb.net/"

client=AsyncIOMotorClient(MONGO_URL)
database=client.mydb

user_collection=database.get_collection("users")

post_collection=database.get_collection("posts")