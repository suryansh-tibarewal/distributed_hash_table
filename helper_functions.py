import random
from constants import key_size

# clockwise ring distance
def ring_distance(a, b):
    if a==b: return 0
    elif a<b: return b-a
    else: return (((10**key_size)-1)+(b-a))

# fixed digits random number
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def generate_hash(key_name):
    key_id = abs(hash(key_name)) % (10 ** key_size)
    return key_id