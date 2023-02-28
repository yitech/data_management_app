from pymongo import MongoClient
from typing import List, Dict


class CRUD:
    def __init__(self):
        self.conn = MongoClient()

    def create(self, db, collection, **document):
        # Insert the document into the collection
        result = self.conn[db][collection].insert_one(document)
        return result.inserted_id

    def read(self, db, collection, **criteria) -> List[Dict]:
        # Find documents in the collection that match the specified criteria
        documents = self.conn[db][collection].find(criteria)
        # Print each document to the console
        return list(documents)

    def update(self, db, collection, params, **criteria):
        # Update a single document in the collection
        result = self.conn[db][collection].update_one(
            criteria,
            {"$set": params}
        )
        return result.matched_count

    def delete(self, db, collection, **document):
        # Delete a single document from the collection
        result = self.conn[db][collection].delete_one(document)
        return result.deleted_count







