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

collection.delete_one({"_id": 2})

query = {"name": {"$regex": "new"}}
res = collection.delete_many(query)
print(f"deleted: {res.deleted_count}")

res = collection.delete_many({})
print(f"deleted: {res.deleted_count}")


print("OK")