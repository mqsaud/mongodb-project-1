import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not Connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_many({"nationality": "american"}, {"$set": {"hair_color": "orange"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
