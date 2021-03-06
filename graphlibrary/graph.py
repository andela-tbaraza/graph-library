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

    def vertices(self):
        """ returns the nodes of a graph """
        return list(self.__graph.keys())

    def remove_vertex(self, node):
        """This method removes a node from the graph dictionary,
        together with all edges connected to it provided that
        node exists.
        """
        if node in self.__graph:
            connections = self.__graph[node]
            del self.__graph[node]  # deletes the node and the edges
            for vertex in connections:
                if node in self.__graph:
                    self.__graph[vertex].remove(node)

        return "node {} has been removed".format(node)

    def adjacent_vertices(self, node):
    	"""This method returns all of the vertices that are
        adjacent to the specified vertex.
        """
        return self.__graph[node]

    def add_edge(self, edge):
        """Adds an edge which is of type list
        and between two nodes there can be multiple edges but
        this method works only if the nodes connecting the edge
        are present
        """
        if type(edge) == list and len(edge) == 2:
            if edge[0] and edge[1] in self.__graph:
                self.__graph[edge[0]].append(edge[1])
                self.__graph[edge[1]].append(edge[0])
            return "Edge created"
        return "Wrong input"

    def add_edges(self, edge_tuple):
     	"""This method allows you to add a tuple of lists of vertices
          but the nodes connecting the edges have to be present
          in the in the dictionary containing the graph.
        """
        if type(edge_tuple) == tuple:
            for edge_list in edge_tuple:
                    if edge_list[0] != edge_list[1]:
                        self.__graph[edge_list[0]].append(edge_list[1])
                        self.__graph[edge_list[1]].append(edge_list[0])
            return True
        return False

    def get_edges(self):
        """ This method generates the edges of the
        graph "__graph". Edges are represented as tuples
        """
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if (node, neighbour) not in edges:
                    edges.append((node, neighbour))
        return edges

    def get_graph(self):
        return self.__graph

    def bfs(self, start, end=None):
        """This methode implements graph traversal using
        breadth first search algorithm. If you specify the
        end node it will give the path from the start node
        to end node otherwise if end node is not specified
        the path to the end of the graph is provided.
        """
        path = []
        queue = deque([start])

        while len(queue) > 0:
            vertex = queue.popleft()
            if vertex in path:
                    continue

            path.append(vertex)

            READY = [node for node in self.__graph[vertex] if node not in path]
            queue.extend(READY)

            if vertex == end:
                return path

        if end == None:
            return path
        else:
            return None

    def dfs(self, start, end=None):
        """This method implements graph traversal using
        depth first search algorithm. If you specify the
        end node it will give the path from the start node
        to end node otherwise if end node is not specified
        the path to the end of the graph is provided.
        """
        path = []
        stack = [start]

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex in path:
                continue

            path.append(vertex)

            READY = [ node for node in self.__graph[vertex] if node not in path]
            stack.extend(READY[::-1])

            if vertex == end:
                return path

        if end == None:
            return path
        else:
            return None

    def generate_graph(self):
        """This method generates a graph in a DOT format
        to enable visualization of the graph.
        """
    	if self.__graph == {}:
        	print "Graph is empty"
        else:
            graph_image = "graph { "
            for key in self.__graph:
                if self.__graph[key] == []:
                    graph_image += key + "; "
                else:
                    for value in self.__graph[key]:
                        if value >= key:
                            graph_image += key + " -- " + value + "; "

            graph_image += "}"

        import webbrowser
        webbrowser.open('http://www.webgraphviz.com/')
        return graph_image


    def generate_graph_traversal(self, path):
        """This method converts the traversed path into a
        DOT format for visualization.
        """
        path_image = "graph { "
        path_image += " -- ".join(path)
        path_image += "; }"

        return path_image

    def generate_image_file(self, image_name, node_list):
    	"""This method generates the file to be used
        for visualization.
        """
        image_file_name = image_name + ".gv"
        image_file = open(image_file_name, "w")
        image_file.write(node_list)
        image_file.close()

    def view_graph(self):
    	"""This method creates a file directly in containing the graph with
        a .gv extension for use in graphviz package for drawing
        the graph.
        """
        graph_image = self.generate_graph()
        return self.generate_image_file("graph_image", graph_image)
