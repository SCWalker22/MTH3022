import itertools

class Node:
    def __init__(
        self,
        name: str,
        connected_nodes: list[str]
    ):
        self.name: str = name
        self.connected_nodes: list[str] = connected_nodes

def find_missing_vertices(
    nodes: list[Node]
    ) -> list[tuple[str, str]]:
    node_names = [n.name for n in nodes]
    possible_combs = list(itertools.combinations(node_names, 2))
    for node in nodes:
        node_combs = [(node.name, n) for n in node.connected_nodes]
        for comb in node_combs:
            if comb in possible_combs: # Check that the node is there before we remove
                possible_combs.remove(comb)
    missing_combinations = possible_combs
    return missing_combinations

def find_polynomial(
    nodes: list[Node]
    ):
    """
    """
    missing_vertices = find_missing_vertices(nodes)
    if missing_vertices != []:
        missing_vertex = missing_vertices[0]
        conns = []
        sub_vertices_1 = [Node(missing_vertex, conns)] + [node for node in nodes if not node.name in missing_vertex]

A = Node("A", ["B", "C", "D"])
B = Node("B", ["C", "D", "E", "F"])
C = Node("C", ["D"])
D = Node("D", ["E", "F"])
E = Node("E", ["F"])
F = Node("F", [])

nodes = [A, B, C, D, E, F]
missing_vertices = find_missing_vertices(nodes)