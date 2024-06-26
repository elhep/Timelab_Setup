#!/usr/bin/env python
import os
import csv
import pprint

from dotenv import load_dotenv
from flask import Flask, request, abort
from pymongo import MongoClient
from urllib.parse import urlparse
from myinflux.utils import csv_to_line_proto
from auth.auth import issue
from collectee import ops

load_dotenv()

app = Flask(__name__)

mongo_url = os.environ.get("MONGODB_URL", "~invalid~")

client = MongoClient(os.environ.get("MONGODB_URL"))

@app.route('/')
def todo():
    return 'Hello from measurement API'

@app.route('/insert/<path:path>', methods=['POST'])
def insert(path):
    if not request.data:
        abort(400, 'Empty request data')
    measNames = _get_meas_names_from_path(path)
    my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    return csv_to_line_proto(request.data.decode('ascii'), my_dictionary, measNames)

@app.route('/tok')
def tok():
    my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    whom = "dupa"
    return issue(whom, my_dictionary)

@app.route('/collectee/add/<name>', methods=['POST'])
def collectee_add(name):
    if not request.json:
        abort(400, 'Bad request data, expecting json')
    return ops.insert(client, name, request.json["description"], request.json["tags"])

@app.route('/collectee/del', methods=['POST'])
def collectee_del():
    if not request.json:
        abort(400, 'Bad request data, expecting json')

    res = ops.delete(client, request.json["ids"])
    if res['status'] != 'ok':
        return res
    #TODO: delete auths
    return res

@app.route('/collectee/get/<id>', methods=['GET'])
def collectee_get(id):
    if id == 'all':
        id = None
    res = ops.get(client, id)
    return res

def _get_meas_names_from_path(path):
    ppath = urlparse(path).path
    return ppath.split('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
