from pymongo.mongo_client import MongoClient


uri = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client.DataBase
collection = db.users

res = collection.insert_one({"id": 1, "name": "test"})
print("Data successfully inserted!")

res = collection.find()
# print(res)

for value in res:
    print(value)