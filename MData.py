from pymongo import MongoClient


class MData:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.affiliates
        self.collections = self.db.companies

    def put_json(self, j_dict):
        post_id = self.collections.insert_one(j_dict).inserted_id
        print("post_id " + str(post_id))
