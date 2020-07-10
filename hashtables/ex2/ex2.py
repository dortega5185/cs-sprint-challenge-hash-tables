
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # prepopulate an array with the same number elements as tickets
    destinations = [None] * length

    destination_lookup = dict()

    # go through each ticket and store its immediate destination
    for i in tickets:
        destination_lookup[i.source] = i.destination
    
    # the starting ticket has a source of "NONE". Start there to build a chain
    next_destination = destination_lookup["NONE"]

    # look up each ticket's next destination and add it to the destinations array
    # stop when the next destination is actually the string "NONE".
    for current_leg in range(0, length):
        # record next destination
        destinations[current_leg] = next_destination        

        # retrieve next destination
        next_destination = destination_lookup[next_destination]

    return destinations
    
