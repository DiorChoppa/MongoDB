from pymongo.mongo_client import MongoClient


user = ''
with open('user') as file:
    user = file.read()

uri = f"mongodb+srv://{user}@database.k537xfr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.testdata
collection = db.users

current = {"name": "test3"}
new_data = {"$set": {"name": "new"}}
collection.update_one(current, new_data)

current = {"_id": 1}
new_data = {"$inc": {"balance": -100}}
collection.update_one(current, new_data)

current = {"_id": 5}
new_data = {"$pop": {"flags": 1}}
collection.update_one(current, new_data)

current = {"_id": 6}
new_data = {"$pull": {"flags": 3}}
collection.update_one(current, new_data)

current = {"_id": 7}
new_data = {"$pop": {"flags": -1}}
collection.update_one(current, new_data)


print("OK")