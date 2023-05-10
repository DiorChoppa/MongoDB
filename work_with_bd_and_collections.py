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

res = collection.count_documents({})
print(res)

res = collection.count_documents({"name": {"$regex": "test."}})
print(res)

res = client.list_database_names()
print(res)

res = db.list_collection_names()
print(res)

# Удалить коллекцию
collection.drop()