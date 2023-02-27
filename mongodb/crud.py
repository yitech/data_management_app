from pymongo import MongoClient


class Role:
    def __init__(self):
        self.conn = MongoClient()
        self.db = self.conn['role']

    def create(self, db, collection, **document):
        # Insert the document into the collection
        result = self.conn[db][collection].insert_one(document)
        return result.inserted_id

    def read(self, db, collection, **criteria):
        # Find documents in the collection that match the specified criteria
        documents = self.conn[db][collection].find(criteria)
        # Print each document to the console
        for document in documents:
            print(document)
        return

    def update(self, db, collection, **document):
        return

    def delete(self, db, collection, **document):
        # Delete a single document from the collection
        result = self.conn[db][collection].delete_one(document)
        return result.deleted_count







