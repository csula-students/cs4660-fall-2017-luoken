"""
Searches module defines all different search algorithms
"""

from graph import graph as g
from queue import Queue

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    #use a queue for this one
    q = Queue()
    q.put(initial_node)

    '''
    pop off initial

    get the list of neigbors

    add each to the queue if not already inside

    if inside list already skip

    else pop

    graph has adjacent, returns true if node 1 and node 2 are directly connected

    neighbors(node) returns all nodes that is adjacenct from node

    edge

    '''
    iterated = []
    path = []
    d = 0 #this will be for the distance. increment once each time you go to next level
    
    #will be how far it is for one to traverse to the next node
    distance = {}
    #will be for parents
    parents = {}

    #maps through the entire list
    while q:
        if(q.empty()):
            break
        
        current = q.get(0) #get the first element

        if current not in iterated: #if its not in iterated, add it to iterated to keep track of all the items iterated through
            iterated.append(current)
            
        for node in graph.neighbors(current):
            if(bool(parents) == False):
                parents[current] = None
                parents[node] = current
            else:
                if node not in parents:
                    parents[node] = current

            q.put(node)
            
    if dest_node in parents: #checks to see if the destination node is in parents, continue
        current = dest_node
        while parents[current]:
            for node in parents:
                if current == node:
                    path.append(g.Edge(parents[node], current, graph.weight(parents[node],current)))
                    current = parents[node]

    path = path[::-1]
    return path
        
def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    #probably use recursion to keep searching or use stack
    
    pass

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
