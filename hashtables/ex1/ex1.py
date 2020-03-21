#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # iterate over weights
    for idx in range(length):
        # check if corresponding weight to equal limit exists in hashtable
        if hash_table_retrieve(ht, limit - weights[idx]) != None:
            # return idx of both weights as:
            # (larger_idx, smaller_idx)
            if idx >= hash_table_retrieve(ht, limit - weights[idx]):
                return (idx, hash_table_retrieve(ht, limit - weights[idx]))
            else:
                return (hash_table_retrieve(ht, limit - weights[idx]), idx)
        # if corresponding weight does not exist, store current weight into hashtable
        else:
            # store weights in hash table such that:
            # key = weight
            # value = idx
            hash_table_insert(ht, weights[idx], idx)
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
