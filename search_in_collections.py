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

query = {"status": True}
for value in collection.find(query, {"_id": 0, "status": 1, "time": 1}):
    print(value)
print("-"*66)

query = {"name": {"$gt": "t"}}
for value in collection.find(query):
    print(value)
print("-"*66)

query = {"name": {"$regex": "test*"}}
for value in collection.find(query):
    print(value)
print("-"*66)

res = collection.find_one({"name": "test3"})
print(res)
print("-"*66)

for value in collection.find().limit(3):
    print(value)
print("-"*66)

for value in collection.find().sort("_id", -1):
    print(value)
print("-"*66)


print("OK")