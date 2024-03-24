import os
import pymongo
import urllib.parse

os.environ["DATABASE_NAME"] = "ReverseImageSearchEngine"
os.environ["ATLAS_CLUSTER_USERNAME"] = "miniproject"
os.environ["ATLAS_CLUSTER_PASSWORD"] = "mini@1212"

class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            # Escape username and password
            escaped_username = urllib.parse.quote_plus(os.environ['ATLAS_CLUSTER_USERNAME'])
            escaped_password = urllib.parse.quote_plus(os.environ['ATLAS_CLUSTER_PASSWORD'])
            # Construct MongoDB connection URI
            uri = f"mongodb+srv://{escaped_username}:{escaped_password}@reverseimagesearch.imkelpv.mongodb.net/?retryWrites=true&w=majority"
            MongodbClient.client = pymongo.MongoClient(uri)
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
