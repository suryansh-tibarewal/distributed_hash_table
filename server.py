import random
import bisect
from helper_functions import ring_distance, random_with_N_digits
from global_variables import *

def get_dht(key_id, partition_id):
    if (partition_id and (partition_id in dht)):
        hash_table = dht[partition_id]
        if (key_id and key_id in hash_table):
            return hash_table[key_id]
    return False

def put_dht(key_id, value, partition_id):
    if (partition_id and (partition_id in dht)):
        hash_table = dht[partition_id]
        if (key_id and value):
            hash_table[key_id] = value
            return True
    return False

def del_dht(key_id, partition_id):
    if (partition_id and (partition_id in dht)):
        hash_table = dht[partition_id]
        if (key_id):
            status = hash_table.pop(key_id, None)
            if status:
                return True
            else:
                # key does not exist
                return False
    return False

def redistribute_keys_join(partition_redistribute_from, partition_redistribute_to):
    hash_table_from = dht[partition_redistribute_from]
    hash_table_to = dht[partition_redistribute_to]
    hash_table = dict(hash_table_from)
    for key_id in hash_table:
        if (ring_distance(partition_redistribute_to, key_id) < ring_distance(partition_redistribute_from, key_id)):
            hash_table_to[key_id] = hash_table_from[key_id]
            del hash_table_from[key_id]
    return

def redistribute_keys_leave(partition_redistribute_from, partition_redistribute_to):
    hash_table_from = dht[partition_redistribute_from]
    hash_table_to = dht[partition_redistribute_to]
    for key_id in hash_table_from:
        hash_table_to[key_id] = hash_table_from[key_id]
    del dht[partition_redistribute_from]
    return

def join(partition_id = None):
    if not partition_id:
        partition_id = random_with_N_digits(16)
    dht[partition_id] = dict()
    partition_ring[partition_id] = dict()
    if not partition_list:
        partition_list.append(partition_id)
        partition_ring[partition_id]['prev'] = partition_id
        partition_ring[partition_id]['next'] = partition_id
    else:
        insert_partition_index = bisect.bisect_left(partition_list, partition_id)
        prev_partition_index = insert_partition_index - 1 # for insert_partition_index 0, it will be -1 means last entry
        prev_partition_id = partition_list[prev_partition_index]
        temp = partition_ring[prev_partition_id]['next']
        partition_ring[prev_partition_id]['next'] = partition_id
        partition_ring[partition_id]['prev'] = prev_partition_id
        partition_ring[partition_id]['next'] = temp
        partition_ring[temp]['prev'] =  partition_id
        bisect.insort_left(partition_list, partition_id)
        redistribute_keys_join(partition_ring[partition_id]['prev'], partition_id)
    # sync_partition_ring_client()
    return partition_id 

def leave(partition_id = None):
    if not partition_id:
        partition_id = random.choice(partition_list)
    if partition_id not in partition_list:
        return False
    if len(partition_list) == 1:
        print "No servers left"
        del partition_ring[partition_id]
        del partition_list[bisect.bisect_left(partition_list, partition_id)]
        del dht[partition_id]
        return True
    prev_partition_id = partition_ring[partition_id]['prev']
    next_partition_id = partition_ring[partition_id]['next']
    partition_ring[prev_partition_id]['next'] = next_partition_id
    partition_ring[next_partition_id]['prev'] = prev_partition_id
    redistribute_keys_leave(partition_id, partition_ring[partition_id]['prev'])
    del partition_ring[partition_id]
    # sync_partition_ring_client()
    del partition_list[bisect.bisect_left(partition_list, partition_id)]
    return True