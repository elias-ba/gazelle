from gazelle import Node, Graph

G = Graph.read_schema("./schemas/schema.json")

print(G.has_path("eliaswalyba", "medteck"))