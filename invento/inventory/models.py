# from django.db import models

# Create your models here.

from pymongo import MongoClient
import pymongo
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.database import Database


def get_db_handle(db_name, host, port, username, password) -> Database:

    client: MongoClient = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    res: Database = client[db_name]
    return res


def get_collection(collectionName) -> Collection:
    client = get_db_handle("invento", "localhost", "27017", "emman-pip", "108996")
    return client[collectionName]
