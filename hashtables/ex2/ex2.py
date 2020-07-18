#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Set up tickets hash table
    tickets_tbl = {}

    # Iterate through the tickets
    for ticket in tickets:
        # Set the source as the key and destination as the value
        tickets_tbl[ticket.source] = ticket.destination

    # Set up route list
    # Initialize with the first location
    route = [tickets_tbl["NONE"]]

    # Find the next destination based on the previous location
    # and append to the route
    for i in range(1,length):
        route.append(tickets_tbl[route[i - 1]])

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

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#            "SLC", "PIT", "ORD", "NONE"]



