from pymongo import MongoClient
from scripts.constants.app_configurations import parser
# import configparser


mongo_uri = parser.get('MONGODB','mongo_uri')
db = parser.get('MONGODB','db_name')


class Mongolite:

    def __init__(self):
        self.connection = MongoClient(mongo_uri)
        self.db = self.connection[db]

    def for_insert_one(self, collection, dictionary):
        collection_1 = self.db[collection]
        if collection_1.insert_one(dictionary.dict()):
            return True
        else:
            return False

    def for_find_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.find_one(data):
            return True
        else:
            return False

    def for_delete_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.delete_one(data):
            return True
        else:
            return False


mongo = Mongolite()