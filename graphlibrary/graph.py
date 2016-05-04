from collections import deque

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

    def add_vertices(self, *args):
        '''This method facilitates the addition of vertices to
        the graph. It takes a list of nodes and adds all of
        them to the graph'''

        for node in args:
            if node not in self.__graph:
                self.__graph[node] = []
        return self

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

    def adjacent_vertices(self, node):
		'''This method returns all of the vertices that are
		adjacent to the specified vertex.'''

		return self.graph[node] 

    def add_edge(self, edge):
        """Adds an edge which is of type set
        and between two nodes there can be multiple edges but
        this method works only if the nodes connecting the edge
        are present
        """
        if type(edge) == list and len(edge) == 2:
            if edge[0] == edge[1]:
                self.__graph[edge[0]].append(edge[1])
            else:
                self.__graph[edge[0]].append(edge[1])
                self.__graph[edge[1]].append(edge[0])
            return True
        return False

    def add_edges(self, edge_list):
    	"""This method allows you to add list of sets of vertices
        but the nodes connecting the edges have to be present
        in the in the dictionary containing the graph
        """ 
        if type(edge_list) == set:
            for sets in edge_list:
                for node_one, node_two in sets:
                    if node_one == node_two:
                        self.graph[node_one].append(node_two)
                    else:
                        self.graph[node_one].append(node_two)
                        self.graph[node_two].append(node_one)

    def get_edge(self):
        """ A static method generating the edges of the
        graph "graph". Edges are represented as sets
        with one (a loop back to the vertex) or two
        vertices
        """
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if [neighbour, node] not in edges:
                    edges.append([node, neighbour])
        return edges



    def get_graph(self):
        return self.__graph

    def bfs(self, start, end=None):
        """This methode implements graph traversal using
        breadth first search algorithm.
        """
        path = []
        queue = deque([start])

        while len(queue) > 0:
            vertex = queue.popleft()
            if vertex in path:
                continue

            path.append(vertex)

            if vertex == end:
                return path

            push_list = [node for node in self.__graph[vertex] if node not in path]
            queue.extend(push_list)

        if end == None:
            return path
        else:
            return None

    def dfs(self, start, end=None):
        path = []
        stack = [start]

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex in path:
                continue

            path.append(vertex)

            if vertex == end:
                return path

            push_list = [node for node in self.__graph[vertex] if node not in path]
            stack.extend(push_list[::-1])

        if end == None:
            return path
        else:
            return None

g = Graph({'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B'], 'E': ['B'], 'F': ['C'], 'G': ['C']})
print g.nodes()
print g.add_edge('L')
print g.add_edges((['A', 'C'], ['B', 'D']))
print g.get_edge()
# print g.dfs('A')
# print g.bfs('A')
# print g.dfs()
# print g.get_edges()
# a = g.get_graph()
# # nx.draw(a)
print g.get_graph()


