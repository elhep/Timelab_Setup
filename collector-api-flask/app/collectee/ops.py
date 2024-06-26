#!/usr/bin/env python
import os

from bson.json_util import dumps, ObjectId

def get(mongo_client, _id = None):
    db = mongo_client['collector']
    collectees = db['collectees']
    result_list = list()
    if _id:
        result_list.append(collectees.find_one({'_id': ObjectId(_id)}))
    else:
        result_list = list(collectees.find())
    for result in result_list:
        result['_id'] = str(result['_id'])
    return result_list

def insert(mongo_client, short_name, description, extra_tags):
    db = mongo_client['collector']
    collectees = db['collectees']
    _id = collectees.insert_one({'short_name': short_name, 'description': description, 'extra_tags': extra_tags})
    if _id.inserted_id:
        return {'status': 'ok', '_id': str(_id.inserted_id)}
    else:
        return {'status': 'error'}

def delete(mongo_client, id_array):
    db = mongo_client['collector']
    collectees = db['collectees']
    obj_id_list = []
    for id in id_array:
        obj_id_list.append(ObjectId(id))
    filter_ids = {"$in": obj_id_list}
    filter = { '_id': filter_ids }

    res = collectees.delete_many(filter)
    if res.deleted_count:
        return {'status': 'ok', 'count': res.deleted_count}
    else:
        return {'status': 'error'}

def edit_description(mongo_client, _id, description):
    pass

def add_auth(mongo_client, collectee_id, auth):
    db = mongo_client['collector']
    collectees = db['collectees_auth']
    _id = collectees.insert_one({'collectee_id': ObjectId(collectee_id), 'auth': auth})
    if _id.inserted_id:
        return {'status': 'ok', '_id': dumps(_id.inserted_id)}
    else:
        return {'status': 'error'}

def update_auth(mongo_client, _id, auth):
    db = mongo_client['collector']
    collectees = db['collectees_auth']
    newvalues = { "$set": { 'auth': auth } }
    filter = { '_id': ObjectId(_id) }
    res = collectees.update_one(filter, newvalues)
    if res.modified_count == 1:
        return {'status': 'ok'}
    else:
        return {'status': 'error'}
