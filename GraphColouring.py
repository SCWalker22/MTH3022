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

def append_unique(
        list_a: list,
        list_b: list
    ) -> list:
    """
    """
    unique_list = list(set(list_a + list_b))
    return unique_list

def replace_connections(
    nodes: list[Node],
    map: dict[str, str]
    ) -> list[Node]:
    """
    
    """
    for node in nodes:
        node.connected_nodes = [map.get(n, n) for n in node.connected_nodes]
    return nodes

def find_polynomial(
    nodes: list[Node]
    ) -> str:
    """
    """
    missing_vertices = find_missing_vertices(nodes)
    print(missing_vertices)
    if missing_vertices != []:
        missing_vertex = missing_vertices[0]
        node_first_conns = [node for node in nodes if node.name == missing_vertex[0]][0].connected_nodes
        node_second_conns = [node for node in nodes if node.name == missing_vertex[1]][0].connected_nodes
        conns = append_unique(node_first_conns, node_second_conns)
        sub_vertices_1 = [Node(missing_vertex, conns)] + [node for node in nodes if not node.name in missing_vertex]
        sub_vertices_1 = replace_connections(sub_vertices_1, {missing_vertex[1]: missing_vertex[0]})
        polynomial_1: str = find_polynomial(sub_vertices_1)
        sub_vertices_2 = [node if node.name != missing_vertex[0] else Node(node.name, node.connected_nodes + [missing_vertex[1]]) for node in nodes]
        polynomial_2: str = find_polynomial(sub_vertices_2)
        total_polynomial: str = f"{polynomial_1} + {polynomial_2}"
    else:
        num_nodes = len(nodes)
        total_polynomial: str = f"K{num_nodes}"
    return total_polynomial


A = Node("A", ["B", "C", "D"])
B = Node("B", ["C", "D", "E", "F"])
C = Node("C", ["D"])
D = Node("D", ["E", "F"])
E = Node("E", ["F"])
F = Node("F", [])

nodes = [A, B, C, D, E, F]
missing_vertices = find_missing_vertices(nodes)
print(missing_vertices)
missing_vertex = missing_vertices[0]
node_first_conns = [node for node in nodes if node.name == missing_vertex[0]][0].connected_nodes
node_second_conns = [node for node in nodes if node.name == missing_vertex[1]][0].connected_nodes
conns = append_unique(node_first_conns, node_second_conns)
sub_vertices_1 = [Node(missing_vertex[0], conns)] + [node for node in nodes if not node.name in missing_vertex]
sub_vertices_1 = replace_connections(sub_vertices_1, {missing_vertex[1]: missing_vertex[0]})
for node in sub_vertices_1:
    print(vars(node))
missing_vertices = find_missing_vertices(sub_vertices_1)
print(missing_vertices)
missing_vertex = missing_vertices[0]
node_first_conns = [node for node in nodes if node.name == missing_vertex[0]][0].connected_nodes
node_second_conns = [node for node in nodes if node.name == missing_vertex[1]][0].connected_nodes
conns = append_unique(node_first_conns, node_second_conns)
sub_vertices_1 = [Node(missing_vertex[0], conns)] + [node for node in nodes if not node.name in missing_vertex]
sub_vertices_1 = replace_connections(sub_vertices_1, {missing_vertex[1]: missing_vertex[0]})
sub_vertices_1_ordered = sorted(sub_vertices_1, key=lambda x: len(x.connected_nodes), reverse=True)
for node in sub_vertices_1_ordered:
    print(vars(node))
missing_vertices = find_missing_vertices(sub_vertices_1)
print(missing_vertices)
# print(find_polynomial(nodes))