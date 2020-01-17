#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    if length == 1:
      return None

    for i in range(len(weights)):
      hash_table_insert(ht, weights[i], i)
    
    for i in range(len(weights)):
      value = limit - weights[i]
      found = hash_table_retrieve(ht, value)
      if found is not None:
        if found > i:
          return (found, i)
        else:
          return (i, found)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

ht = HashTable(5)
hash_table_insert(ht, 4, 0)
hash_table_insert(ht, 4, 1)
print(hash_table_retrieve(ht, 4))

