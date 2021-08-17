from lib.node import Node
from typing import List
from pyvis.network import Network
import networkx as nx

class Graph:

    SEARCH_ALGORITHMS = {
        "BFS": "bfs",
        "DFS": "dfs"
    }

    def __init__(self, schema: List[Node]):
        self.schema = schema
        self.adj_list = self.compute_adj_list()

    def compute_adj_list(self, schema=None, adj_list={}):
        name = self.schema.state["name"] if schema is None else schema.state["name"]
        sons = self.schema.sons if schema is None else schema.sons
        adj_list[name] = [son.state["name"] for son in sons]
        for son in sons:
            self.compute_adj_list(son, adj_list)
        return adj_list

    def search_node(self, source_node, value, algorithm):
        if source_node not in self.adj_list.keys():
            return None, 0
        to_visit, cpt = [source_node], 1
        while(len(to_visit) > 0):
            if algorithm == Graph.SEARCH_ALGORITHMS["BFS"]:
                node = to_visit.pop(0) 
            elif algorithm == Graph.SEARCH_ALGORITHMS["DFS"]:
                node = to_visit.pop()
            else:
                return None, 0
            if node == value:
                return value, cpt
            to_visit.extend(self.adj_list[node])
            cpt += 1
        return None, cpt

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

    