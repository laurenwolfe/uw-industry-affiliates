from pymongo import *


class MData:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.affiliates
        self.collection = self.db.companies

    def put_json(self, j_dict):
        post_id = self.collection.insert_one(j_dict)
        post_id = post_id.inserted_id
        if not post_id:
            print("no new id returned")
        else:
            print(post_id)
        return post_id

    def clear_collection(self):
        self.collection.delete_many(({}))
        # self.collection.create_index([('co_name',  )])
