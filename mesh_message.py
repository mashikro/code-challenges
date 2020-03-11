# You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.

# Instead of routing texts through cell towers, your app sends messages via the phones 
# f nearby users, passing each message along from one phone to the next until it reaches 
# the intended recipient. (Don't worry—the messages are encrypted while they're in transit.)

# Some friends have been using your service, and they're complaining that it takes a 
# long time for messages to get delivered. After some preliminary debugging, you suspect 
# messages might not be taking the most direct route from the sender to the recipient.

# THINK: Shortest path aka 0BFS

# Given information about active users on the network, find the shortest route for a 
# message from one user (the sender) to another (the recipient). Return a list of users that make up this route.

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam'],
    'Noam'    : [ 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min']
}

# Jayden to Adam:   ['Jayden', 'Amelia', 'Adam']
def reconstruct_path(path_of_message, sender, recipient):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current = recipient
    while current:
        reversed_shortest_path.append(current)
        current = path_of_message[current]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed

# network is a graph in adjacency list format. Graph is undirected and unweighted. 
# Ex Min and Jayden are both in each other's neighbor list

from collections import deque

def find_shortest_path(network, sender, recipient):
    '''Finding shortest path between sender and recipient'''
    
    if sender not in network:
        raise Exception('Sender not in network')
    if recipient not in network:
        raise Exception('Recipient not in network')
    
    #this is a queue that will help us do BFS
    to_visit = deque()
    to_visit.append(sender)    


    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've
    # already visited SO we dont do extra work
    path_of_message = {sender: None} #bc path starts with sender
    
    while to_visit: #while their is items in the queue
        
        current = to_visit.popleft() #pop first item FIFO

        # Stop when we reach the end node
        if current == recipient:
            return reconstruct_path(path_of_message, sender, recipient)

        # populate path_of_message here
        for neighbor in network[current]: #Looping through current's friends
            if neighbor not in path_of_message: #if we havent already checked it
                to_visit.append(neighbor)
                path_of_message[neighbor] = current

    # If we get here, then we never found the end node
    # so there's NO path from start_node to end_node
    return None


print(find_shortest_path(network, 'Jayden', 'Adam')) #'Jayden', 'Amelia', 'Adam']

print(find_shortest_path(network, 'Jayden', 'Amelia')) #'Jayden', 'Amelia'

print(find_shortest_path(network, 'Min', 'Adam')) #[Min, 'Jayden', 'Amelia', 'Adam']


# Runtime: complexity of the breadth-first search is O(N+M).












