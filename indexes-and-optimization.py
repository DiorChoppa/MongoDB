import pymongo
from itertools import count
import datetime


user = ''
with open('user') as file:
    user = file.read()

uri = f"mongodb+srv://{user}@database.k537xfr.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
try:
    client.admin.command('ping')
except Exception as e:
    print("ERROR!")
    print(e)

db = client.testdata
collection = db.users

# for i in count(0, 1):
#     data = {
#         "_id": i,
#         "login": f"name{i}",
#         "password": f"passw{i}",
#         "time": datetime.datetime.now()
#     }
#     collection.insert_one(data)
#     print(f"{i}: data written!")

collection.drop_index("login_-1")
collection.create_index([("login", pymongo.DESCENDING)], unique=True)
print(collection.index_information())
print(collection.find_one({"login": "name111"}))