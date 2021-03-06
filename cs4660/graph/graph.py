# """
# graph module defines the knowledge representations files

# A Graph has following methods:

# * adjacent(node_1, node_2)
#     - returns true if node_1 and node_2 are directly connected or false otherwise
# * neighbors(node)
#     - returns all nodes that is adjacency from node
# * add_node(node)
#     - adds a new node to its internal data structure.
#     - returns true if the node is added and false if the node already exists
# * remove_node
#     - remove a node from its internal data structure
#     - returns true if the node is removed and false if the node does not exist
# * add_edge
#     - adds a new edge to its internal data structure
#     - returns true if the edge is added and false if the edge already existed
# * remove_edge
#     - remove an edge from its internal data structure
#     - returns true if the edge is removed and false if the edge does not exist
# """

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object
    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented
    In example, you will need to do something similar to following:
    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    openFile = open(file_path)
    readFile = openFile.read()
    splitByNewLine = readFile.split("\n")
    
    lineSplit = [line.split(":") for line in splitByNewLine if line != ""]
    numberOfNodes = int(lineSplit[0][0])
    restOfLines = lineSplit[1:]

    for node in range(numberOfNodes): # create and add nodes to graph
         graph.add_node(Node(node))

    for lineNumber in restOfLines:
        graph.add_edge(Edge(Node(int(lineNumber[0])), Node(int(lineNumber[1])), int(lineNumber[2])))
        
    openFile.close()

    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other_node):
        return self.data < other_node.data
    def __gt__(self, other_node):
        return self.data > other_node.data


    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))

class AdjacencyList(object):
    """
                             AdjacencyList is one of the graph representation which uses adjacency list to
                                 store nodes and edges
                                     """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if node_1 in self.adjacency_list and node_2 in self.adjacency_list:
            for value in self.adjacency_list[node_1]:
                if value.to_node == node_2:
                    return True
            return False
        else:
            return False

    def neighbors(self, node):
        neighbor = []
        for value in self.adjacency_list[node]:
            neighbor.append(value.to_node)
        return neighbor

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            return True
        else:
            return False

    def remove_node(self, node):
        if node in self.adjacency_list:
            del self.adjacency_list[node]
            for line in self.adjacency_list:
                for val in self.adjacency_list[line]:
                    if val.to_node == node:
                        self.remove_edge(val)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge not in self.adjacency_list[edge.from_node]:
            self.adjacency_list[edge.from_node].append(edge)
            return True
        else:
            return False
        

    def remove_edge(self, edge):
        if edge.from_node in self.adjacency_list:
            if edge in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge)
                return True
            else:
                return False
        return False

    def get_edge_weight(self, node_1, node_2):
        for node in self.adjacency_list[node_1]:
            if(node.from_node == node_1 and node.to_node == node_2):
                return node.weight

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 in self.nodes and node_2 in self.nodes:
            if self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)] != 0:
                return True
            else:
                return False
        else:
            return False

    def neighbors(self, node):
        if node in self.nodes:
            neighbors = []
            node_index = self.__get_node_index(node)
            for x in range(len(self.adjacency_matrix[node_index])):
                if self.adjacency_matrix[node_index][x] != 0:
                    neighbors.append(Node(x))
            return neighbors

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            for x in self.adjacency_matrix:
                x.append(0)
            self.adjacency_matrix.append([0] * len(self.nodes))
            for x in self.adjacency_matrix:
                x.append(0)
            return True
        else:
            return False
    
    def remove_node(self, node):
        if node in self.nodes:
            node_index = self.__get_node_index(node)
            self.nodes.remove(node)
            for val in self.adjacency_matrix:
                del val[node_index]
            del self.adjacency_matrix[node_index]
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            x_val = self.__get_node_index(edge.from_node)
            y_val = self.__get_node_index(edge.to_node)
            if self.adjacency_matrix[x_val][y_val]  == 0:
                self.adjacency_matrix[x_val][y_val] = edge.weight
                return True
            else:
                return False
        else:
            return False

    def remove_edge(self, edge):
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            if self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] != 0:
                self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] = 0
                return True
            else:
                return False
        else:
            return False

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)

    def get_edge_weight(self, node_1, node_2):
        return self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)]

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        #edge has a from_node, to_node, weight
        #edges = 2d array, iterate through everything before returning true of false.
        if node_1 in self.nodes and node_2 in self.nodes:
            for x in self.edges:
                if x.from_node == node_1 and x.to_node == node_2:
                    return True
            return False
        else:
            return False
        
    def neighbors(self, node):
        neighbors = []
        if node in self.nodes:
            for x in self.edges:
                if x.from_node == node:
                    neighbors.append(x.to_node)
            return neighbors

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            return True  
        else:
            return False
        
    def remove_node(self, node):
        if node in self.nodes:
            for x in self.edges:
                if x.to_node == node or x.from_node == node:
                    self.edges.remove(x)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)
            return True
        else:
            return False
        
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False
        
    def get_edge_weight(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return edge.weight

