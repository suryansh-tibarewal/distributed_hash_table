import random
from helper_functions import generate_hash, ring_distance
from server import get_dht, put_dht, del_dht
from global_variables import *

def get_partition_id(key_id):
    if not partition_ring:
        raise NoServerError("Start a server, before using the client")
    current_partition_id = random.choice(partition_ring.keys())
    while ring_distance(current_partition_id, key_id) > \
          ring_distance(partition_ring[current_partition_id]['next'], key_id):
        current_partition_id = partition_ring[current_partition_id]['next']
    return current_partition_id

def get(key_name):
    key_id = generate_hash(key_name)
    partition_id = get_partition_id(key_id)
    value = get_dht(key_id, partition_id)
    if value:
        return value
    else:
        return False

def put(key_name, value):
    key_id = generate_hash(key_name)
    partition_id = get_partition_id(key_id)
    status = put_dht(key_id, value, partition_id)
    return status

def delete(key_name):
    key_id = generate_hash(key_name)
    partition_id = get_partition_id(key_id)
    status = del_dht(key_id, partition_id)
    return status

class NoServerError(Exception):
   """Class for handling exception when no server exists"""
   # this can than be used to decide when to spin up a server
   pass