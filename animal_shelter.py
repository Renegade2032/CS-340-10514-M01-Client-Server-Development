from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """
    AnimalShelter class provides CRUD operations for the Grazioso Salvare project.
    This class connects to MongoDB using authentication and allows Create, Read,
    Update, and Delete actions on the AAC animals collection.
    """

    def __init__(self, username, password,
                 host="127.0.0.1", port=27017,
                 db_name="aac", collection_name="animals"):
        """
        Initialize the MongoDB connection.
        """
        try:
            uri = (
                f"mongodb://{username}:{password}@{host}:{port}/"
                f"{db_name}?authSource={db_name}"
            )

            self.client = MongoClient(uri)
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]

        except PyMongoError as e:
            print(f"Database connection error: {e}")

    def create(self, data):
        """
        Insert a document into the collection.

        Input:
            data (dict): document to insert

        Return:
            True if insert was successful, else False
        """
        if data is None or not isinstance(data, dict):
            return False

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError as e:
            print(f"Create error: {e}")
            return False

    def read(self, query):
        """
        Query documents from the collection using find().

        Input:
            query (dict): filter criteria

        Return:
            List of matching documents if successful, else empty list
        """
        if query is None or not isinstance(query, dict):
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"Read error: {e}")
            return []

    def update(self, query, update_data):
        """
        Update document(s) in the collection.

        Input:
            query (dict): filter criteria
            update_data (dict): update statement (ex: {"$set": {...}})

        Return:
            Number of documents modified
        """
        if (query is None or not isinstance(query, dict) or
                update_data is None or not isinstance(update_data, dict)):
            return 0

        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except PyMongoError as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        """
        Delete document(s) in the collection.

        Input:
            query (dict): filter criteria

        Return:
            Number of documents deleted
        """
        if query is None or not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete error: {e}")
            return 0
