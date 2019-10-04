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
    for weight in weights:
        hash_table_insert(ht, weight, weights.index(weight))
        
    y = 0
    while y != 4:
        for x in range(len(weights)-y):
            print(x)
        y += 1
    return hash_table_retrieve(ht, 16)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)

46
410
415
416
610
615
616
1015
1016
1516

# a for loop that starts at the length of the array minus 1, starts basically you need to take the first one, add the rest, second, add the rest, third, add the rest until you find a sum that equals the limit and stop, could be done recursively