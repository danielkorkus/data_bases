from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

user_name = str(input("insert your user_name: "))
password = str(input("insert your cluster password: "))

cls = f"mongodb+srv://{user_name}:{password}@main-cluster.vxmilan.mongodb.net/test_db?retryWrites=true&w" \
      "=majority"


class DbServer:
    def __init__(self, cluster: str):
        self.cluster = cluster
        self.client = MongoClient(self.cluster)
        self.db = self.client.test_db.test_db

    def test_client(self):
        return self.client.list_database_names()

    def add_new_data(self, data: dict):
        self.db.insert_one(data)

    def remove_data(self, id: str):
        self.db.delete_one({"_id": ObjectId(id)})

    def read_data(self, id: str):
        return self.db.find_one({"_id": ObjectId(id)})

    def find_docs_by_name(self, name: str):
        return self.db.find({"name": name})


server1 = DbServer(cls)

# inserting 10 items
for _ in range(10):
    server1.add_new_data({"name": "Daniel", "text": "My first todo!", "status": "open",
                          "tags": ["python", "coding"], "date": datetime.datetime.now()})

# print(server1.read_data('6.....323'))
# print(server1.find_docs_by_name("Daniel"))
# server1.remove_data('63f216.......23')
