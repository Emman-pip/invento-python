# from django.db import models

# Create your models here.

from pymongo import MongoClient


def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    db_handle = client[db_name]
    return client


def get_collection(collectionName):
    client = get_db_handle("invento", "localhost", "27017", "emman-pip", "108996")
    return client[collectionName]
