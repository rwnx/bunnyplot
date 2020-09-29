import networkx as nx

def info(graph):
    return nx.info(graph)

def write_graphml(graph, path):
    return nx.write_graphml(graph, path)

def build_graph(consumers, definitions):
    queues = definitions["queues"]
    exchanges = definitions["exchanges"]
    bindings = definitions["bindings"]

    graph = nx.DiGraph(name=f"RabbitMQ graph")
    for q in queues:
        graph.add_node(q["name"])
        graph.nodes[q["name"]]["Text"] = q["name"]

    for x in exchanges:
        graph.add_node(x["name"])

    for qx in bindings:
        graph.add_edge(qx["source"], qx["destination"])

    for c in consumers:
        graph.add_node(c["channel_details"]["user"])
        graph.add_edge(c["queue"]["name"], c["channel_details"]["user"])

    return graph
