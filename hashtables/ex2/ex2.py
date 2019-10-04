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
    # this looks like we're building a linked list from a hash table
    # fill up the table
    # loop through the list adding destiations to your source by looking up the destinations from their source in the hash table
    """
    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source,ticket.destination)
    for i in range(len(route)):    
        route[0] = hash_table_retrieve(hashtable, "NONE")
        if i+1 >= len(route):
            return route
        else:
            
            route[i+1] = hash_table_retrieve(hashtable, route[i])
    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
#print(ticket_1.destination)
#reconstruct_trip(tickets, len(tickets))
