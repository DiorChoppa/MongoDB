from pymongo.mongo_client import MongoClient
import datetime


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

collection.insert_one({"_id": 1, "name": "test1"})
collection.insert_one({"_id": 2, "name": "test2"})

data = [
    {
        "_id": 5,
        "name": "test3",
        "time": datetime.datetime.now(),
        "flags": [1, 2, 3]
    },
    {
        "_id": 6,
        "name": "test4",
        "time": datetime.datetime.now(),
        "flags": [1, 2, 3]
    }
]

collection.insert_many(data)


print("OK")