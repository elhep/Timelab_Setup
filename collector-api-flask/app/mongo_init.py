#!/usr/bin/env python
import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING, TEXT, HASHED

load_dotenv()
mongo_url = os.environ.get("MONGODB_URL", "~invalid~")

client = MongoClient(os.environ.get("MONGODB_URL"))

db = client["collector"]

collectees = db["collectees"]
collectees.create_index([("short_name", TEXT)], unique = True)

collectees_auth = db["collectees_auth"]
collectees.create_index([("collectee_id", ASCENDING)], unique = True)
