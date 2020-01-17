#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
      hash_table_insert(hashtable, i.source, i.destination)
    
    start = 'NONE'
    for i in range(len(route)):
      value = hash_table_retrieve(hashtable, start)
      route[i] = value
      start = value

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)
