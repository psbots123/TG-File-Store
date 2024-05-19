import os
from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
# Initialize MongoDB Client
client = AsyncIOMotorClient(DATABASE_URL)
db = client["DATABASE_NAME"]  # Replace "mydatabase" with your database name
collection = db["database"]

# Define your database model as a dictionary
class Database:
    def __init__(self, id, up_name):
        self.id = str(id)
        self.up_name = up_name

# Function to update or insert data
async def update_as_name(id, mode):
    result = await collection.find_one({"_id": id})
    if result:
        await collection.update_one({"_id": id}, {"$set": {"up_name": mode}})
    else:
        new_data = {"_id": id, "up_name": mode}
        await collection.insert_one(new_data)

# Function to get data
async def get_data(id):
    user_data = await collection.find_one({"_id": id})
    if not user_data:
        new_user = {"_id": id, "up_name": False}
        await collection.insert_one(new_user)
        user_data = await collection.find_one({"_id": id})
    return user_data
