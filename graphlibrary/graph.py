class Graph(object):
    """ A graph class that implements a graph data structure
    with the following features:
            - A graph is represented as a dictionary
            - The keys of that dictionary are the nodes(vertices)
            - The values of the dictionary are the edges
    """

    def __init__(self, graph={}):
        if type(graph) == dict:
            self.__graph = graph
        else:
            self.__graph = None

    def add_vertex(self, node):
        """if the node is not in self.__graph:
        a key with an empty list as the value is added
        to the dictionary, else nothing is done
        """
        if node not in self.__graph:
            self.__graph[node] = []
            return True

    def add_vertices(self, *args):
        '''This method facilitates the addition of vertices to
        the graph. It takes a list of nodes and adds all of
        them to the graph'''

        for node in args:
            if node not in self.__graph:
                self.graph[node] = []

    def nodes(self):
        """ returns the nodes of a graph """
        return list(self.__graph.keys())

    def remove_vertex(self, node):
        """This method removes a node from the graph dictionary,
        together with all edges connected to it provided that
        node exists.
        """
        for node in self.__graph:
            if node in self.__graph[node]:
                self.__graph[node].remove(node)
            del self.__graph[node]
            return True

    def add_edge(self, edge):
        """Adds an edge which is of type list, tuple or set
        and between two nodes there can be multiple edges
        """
        if type(edge) == list and len(edge) == 2:
            edge = set(edge)
            (node1, node2) = tuple(edge)
            if node1 in self.__graph:
                self.__graph[node1].append(node2)
            else:
                self.__graph[node1] = [node2]
            return True
        return False

    def get_edges(self):
        """ A static method generating the edges of the
        graph "graph". Edges are represented as sets
        with one (a loop back to the vertex) or two
        vertices
        """
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})
        return edges
