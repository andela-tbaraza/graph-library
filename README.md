# Python Graph Library
[![Build Status](https://travis-ci.org/Tonida/bc-7-graph_library.svg?branch=dev)](https://travis-ci.org/Tonida/bc-7-graph_library)

## Introduction
A graph is a way of representing connections between places. Mathematically, a graph is a collection of nodes and edges. Nodes are locations that are connected together by the edges of the graph. For instance, if you had two small towns connected by a two-way road, you could represent this as a graph with two nodes, each node representing a town, and one edge, the road, connecting the two towns together.
A graph can be directed or undirected. Directed graph is one in which edges connect only one way. This library implements undirected graphs and allows you to create a .dot file that can be used to view the created graphs using [GraphViz](www.graphviz.org)

## Features
This library has the following methods:

**init(self, __graph={}):** This constructor initializes the class. The __ preceding the method makes rhe instance varuable graph to be private, therefore it can't be accessed outside the class. Initializing the class without an input will create an empty dictionary.

**add_vertices(self, *args):** This method adds a vertex or vertices to the graph depending the input as a string. The vertices represent the keys in the graph dictionary.

**vertices(self):** This method outputs all the vertices in the graph. The user doesn't have to supply any parameters as they are obtained from the graph created.

**remove_vertex(self, node):** This method removes a node from the graph dictionary,
together with all edges connected to it provided that node exists.

**adjacent_vertices(self, node):** This method returns all of the vertices that are
adjacent to the specified vertex.

**add_edge(self, node ):** Adds one edge which is of type list and between two nodes there can be multiple edges butthis method works only if the nodes connecting the edges are present.

**add_edges(self, edge_tuple):** This method allows you to add a tuple of lists of vertices but the nodes connecting the edges have to be present in the in the dictionary containing the graph.

**get_edges(self):** This method generates the edges of the graph "__graph". Edges are represented as tuples.

**bfs(self, start, end=None):**This methode implements graph traversal using
breadth first search algorithm. If you specify the end node it will give the path from the start node to end node otherwise if end node is not specified the path to the end of the graph is provided.

**dfs(self, start, end=None):**This method implements graph traversal using depth first search algorithm. If you specify the end node it will give the path from the start node to end node otherwise if end node is not specified the path to the end of the graph is provided.

**generate_graph(self):** This method generates a graph in a DOT format to enable visualization of the graph. Use this web interface to view you graph [view_graph](http://www.webgraphviz.com/).

**draw_graph(self):**This method creates a file containing the graph with a .gv extension for use in graphviz software for drawing the graph directly in an editor.

**To view a demonstration of the library view click on [graph-video](https://asciinema.org/a/csq09waj2siochp1o3w87ev0v)**







