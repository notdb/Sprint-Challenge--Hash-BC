#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    # take the limit, subtract it by everything in the table once
    # then take the reset, query the hash table to see if it's there
    # for example, 21 - 4 = 17, so we see if 17 is in the hash table, if it is, we know 4 and 17 are our answers
    """
    if len(weights) == 1:
        return None
    for weight in weights:
        hash_table_insert(ht, weight, weights.index(weight))
        if hash_table_retrieve(ht, limit - weight) is not None:
            if weights.index(weight) == hash_table_retrieve(ht, limit - weight):
                newList =[weights.index(weight)+1, hash_table_retrieve(ht, limit - weight)]
            else:
                newList = [weights.index(weight), hash_table_retrieve(ht, limit - weight)]
            
    return newList

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

#get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
# a for loop that starts at the length of the array minus 1, starts basically you need to take the first one, add the rest, second, add the rest, third, add the rest until you find a sum that equals the limit and stop, could be done recursively

