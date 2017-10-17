"""
Searches module defines all different search algorithms"""

from graph import graph as g
from queue import Queue, PriorityQueue

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    #use a queue for this one
    q = Queue()
    q.put(initial_node)
    
    iterated = []
    path = []
    parents = {}
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
                    path.append(g.Edge(parents[node], current, graph.get_edge_weight(parents[node],current)))
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
    iterated = []
    path = []
    parents = {}
    stack = []

    stack.append(initial_node)

    while stack:
        current = stack.pop()
        if current not in iterated:
            iterated.append(current)
            temp = []
            for node in graph.neighbors(current):
                if(bool(parents) == False):
                    parents[current] = None
                    parents[node] = current
                if node not in iterated:
                    parents[node] = current
                    temp.append(node)
            temp = temp[::-1]
            
            for t in temp:
                if current in stack:
                    stack.remove(current)
                stack.append(t)

    if dest_node in parents: #checks to see if the destination node is in parents, continue
        current = dest_node
        while parents[current]:
            for node in parents:
               if current == node:
                    path.append(g.Edge(parents[node], current, graph.get_edge_weight(parents[node],current)))
                    current = parents[node]
                    
    path = path[::-1]
    return path

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    pq = PriorityQueue()
    pq.put((0, initial_node))
    path = []

    parent = {}
    cost = {}
    parent[initial_node] = None
    cost[initial_node] = 0

    while not pq.empty():
        current = pq.get()
        # print(graph.neighbors(current[1]))
        # break
        if current[1] == dest_node:
            break
        for node in graph.neighbors(current[1]):
            new_cost = cost[current[1]] + graph.get_edge_weight(current[1], node)

            if node not in cost or new_cost < cost[node]:
                cost[node] = new_cost
                pq.put((new_cost, node))
                parent[node] = current[1]

        
    if dest_node in parent:
        current = dest_node
        while parent[current]:
            for node in parent:
                if current == node:
                    path.append(g.Edge(parent[node], current, graph.get_edge_weight(parent[node], current)))
                    current = parent[node]

    path = path[::-1]

    return path



def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass
