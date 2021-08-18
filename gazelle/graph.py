from gazelle.edge import Edge
import json
from gazelle import Node
from typing import Dict, List
from pyvis.network import Network
import networkx as nx

class Schema:
    def __init__(self, type, nodes, edges):
        self.type = type
        self.nodes = nodes
        self.edges = edges

    def __repr__(self):
        return f"Schema(\n\ttype: {self.type},\n\tnodes: {self.nodes},\n\tedges: {self.edges}\n)"

    def __str__(self):
        return f"Schema(\n\ttype: {self.type},\n\tnodes: {self.nodes},\n\tedges: {self.edges}\n)"

class Graph:

    SEARCH_ALGORITHMS = {
        "BFS": "bfs",
        "DFS": "dfs"
    }

    DIRECTED = "directed"
    UNDIRECTED = "undirected"

    def __init__(self, schema: Schema):
        self.schema = schema
        self.adj_list = self.compute_adj_list()

    def read_schema(schema_file):
        schema_file_extension = schema_file.split(".")[-1]
        if schema_file_extension.lower() != "json":
            raise ValueError(f"{schema_file} should be a json file")
        with open(schema_file) as f:
            data = json.load(f)
            return Graph(Schema(
                data["type"],
                [Node(node) for node in data["nodes"]],
                [Edge(edge) for edge in data["edges"]]
            ))

    def compute_adj_list(self):
        adj_list = {node.state["id"]:[] for node in self.schema.nodes}
        for edge in self.schema.edges:
            if self.schema.type == Graph.DIRECTED:
                adj_list[edge.state["from"]].append(edge.state["to"])
            else:
                adj_list[edge.state["link"][0]].append(edge.state["link"][1])
                adj_list[edge.state["link"][1]].append(edge.state["link"][0])
        return adj_list

    def has_node(self, node_id):
        return node_id in self.schema.nodes

    def has_path(self, source_node, destination_node, algorithm="dfs"):
        if source_node not in self.adj_list.keys():
            return False, 0
        to_visit, cpt = [source_node], 0
        while(len(to_visit) > 0):
            if algorithm == Graph.SEARCH_ALGORITHMS["BFS"]:
                node = to_visit.pop(0) 
            elif algorithm == Graph.SEARCH_ALGORITHMS["DFS"]:
                node = to_visit.pop()
            else:
                raise ValueError(f"Unknown algorithm {algorithm}")
            if node == destination_node:
                return True, cpt
            to_visit.extend(self.adj_list[node])
            cpt += 1
        return False, 0

    def get_edge(self, node_1, node_2):
        if not self.has_path(node_1, node_2)[0]:
            return None
        
    def display(self, path):
        network = nx.Graph()
        for node in self.adj_list.keys():
            network.add_node(node, title=node)
        for node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                network.add_edge(node, neighbor)

        graph = Network('500px', '1000px')
        graph.from_nx(network)
        graph.show(path)

    def search_path(self, source_node, target_node, algorithm):
        pass

    