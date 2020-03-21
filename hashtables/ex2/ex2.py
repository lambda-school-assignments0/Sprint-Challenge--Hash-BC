#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    # iterate through `tickets` array and store `ticket` such that:
    # key = source (ticket[0])
    # value = destination (ticket[1])
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # populate route by appending from value of hashtable starting with key: "NONE"
    for idx in range(length-1):
        if idx == 0:
            route[idx] = hash_table_retrieve(hashtable, "NONE")
        else:
            route[idx] = hash_table_retrieve(hashtable, route[idx-1])

    return route
