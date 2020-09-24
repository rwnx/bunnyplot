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
        id = q["name"]
        graph.add_node(id)
        graph.nodes[id]["name"] = id
        graph.nodes[id]["type"] = "queue"

    for x in exchanges:
        id = x["name"]
        graph.add_node(id)
        graph.nodes[id]["name"] = id
        graph.nodes[id]["type"] = "exchange"

    for qx in bindings:
        source_id = qx["source"]
        destination_id = qx["destination"]
        graph.add_edge(source_id, destination_id)

    for c in consumers:
        id = c["channel_details"]["user"]
        q_id = c["queue"]["name"]
        graph.add_node(id)
        graph.nodes[id]["name"] = id
        graph.nodes[id]["type"] = "consumer"
        graph.add_edge(q_id, id)

    return graph
