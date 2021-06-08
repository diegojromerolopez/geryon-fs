import configparser
import pymongo
from montydb import MontyClient
from pymongo.collection import Collection


class MongoConnector(object):
    CONFIG_SECTION = "mongofs"
    DEFAULT_COLLECTION_NAME = "mongofs-drive"

    def __init__(self, config: configparser.ConfigParser) -> None:
        self.config = config

    def connect(self) -> Collection:
        mongo_backend = self.config.get(section=self.CONFIG_SECTION, option="backend")
        if hasattr(self, f"_MongoConnector__connect_{mongo_backend}"):
            return getattr(self, f"_MongoConnector__connect_{mongo_backend}")()
        raise ValueError(f'Unrecognized backend "{mongo_backend}"')

    def __connect_memory_instance(self) -> Collection:
        database = self.config.get(section=self.CONFIG_SECTION, option="database")
        collection_name = self.config.get(section=self.CONFIG_SECTION, option="collection")
        return MontyClient(":memory:")[database][collection_name]

    def __connect_mongo_server(self) -> Collection:
        username = self.config.get(section=self.CONFIG_SECTION, option="username")
        password = self.config.get(section=self.CONFIG_SECTION, option="password")
        host = self.config.get(section=self.CONFIG_SECTION, option="host")
        database = self.config.get(section=self.CONFIG_SECTION, option="database")
        collection_name = self.config.get(section=self.CONFIG_SECTION, option="collection")
        connection_string = \
            f"mongodb+srv://{username}:{password}@{host}/{database}?retryWrites=true&w=majority"

        client = pymongo.MongoClient(connection_string)
        db = client[database]
        col = db[collection_name]
        col.create_index([("path", pymongo.ASCENDING)], unique=True)
        col.create_index([("path", pymongo.ASCENDING), ("created_at", pymongo.ASCENDING)])
        col.create_index([("path", pymongo.ASCENDING), ("created_at", pymongo.DESCENDING)])
        col.create_index([("path", pymongo.ASCENDING), ("last_updated_at", pymongo.ASCENDING)])
        col.create_index([("path", pymongo.ASCENDING), ("last_updated_at", pymongo.DESCENDING)])
        return col
