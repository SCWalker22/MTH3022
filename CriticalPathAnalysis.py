class Node:
    def __init__(self,
        name: str,
        duration: int,
        preceding: None | list[str],
        following: None | list[str],
        earliest_start: int | None = None,
        earliest_end: int | None = None,
        latest_start: int | None = None,
        latest_end: int | None = None,
        float_time: int | None = None):
        self.name: str = name
        self.duration: int = duration
        self.preceding: list[str] = preceding
        self.following: list[str] = following
        self.earliest_start: int | None = earliest_start
        self.earliest_end: int | None = earliest_end
        self.latest_start: int | None = latest_start
        self.latest_end: int | None = latest_end
        self.float_time: int | None = float_time

def check_nodes(
    nodes: list[Node]
    ) -> bool:
    """
    Check if a provided list of nodes is valid (preceding matches following)
    """
    pass

def print_nodes(
    nodes: list[Node]
    ):
    """
    """
    for node in nodes:
        print(vars(node))

def display(
    nodes: list[Node],
    show_duration: bool = False
    ):
    """
    """
    for node in nodes:
        print_str: str = f"{node.name}, ES = {node.earliest_start}, LS = {node.latest_start}, Float = {node.float_time}"
        if show_duration:
            print_str += f", Duration = {node.duration}"
        print(print_str)

def forward_pass(
    nodes: list[Node]
    ) -> list[Node]:
    """
    Run a forward pass on a list of nodes
    """
    for node in nodes:
        preceding_nodes: list[Node] = [n for n in nodes if n.name in node.preceding]
        preceding_ends: list[int] = [n.earliest_end for n in preceding_nodes]
        if preceding_ends != []:
            last_preceding_end = max(preceding_ends)
        else:
            last_preceding_end = 0
        node.earliest_start = last_preceding_end
        node.earliest_end = node.earliest_start + node.duration
    return nodes

def backward_pass(
    nodes: list[Node]
    ) -> list[Node]:
    """
    """
    for node in reversed(nodes):
        following_nodes: list[Node] = [n for n in nodes if n.name in node.following]
        following_starts: list[int] = [n.latest_start for n in following_nodes]
        print_nodes(following_nodes)
        if following_starts != []:
            earliest_following_ends = min(following_starts)
        else:
            earliest_following_ends = node.earliest_end
        print(earliest_following_ends)
        node.latest_end = earliest_following_ends
        node.latest_start = node.latest_end - node.duration
    return nodes

def calculate_floats(
    nodes: list[Node]
    ) -> list[Node]:
    """
    """
    for node in nodes:
        node.float_time = node.latest_start - node.earliest_start
    return nodes

def find_critical_path(
    nodes: list[Node]
    ) -> list[str]:
    """
    """
    path: list[str] = []
    for node in nodes:
        if node.float_time == 0:
            path.append(node.name)
    return path

A = Node("A", 13, [], ["B", "C"])
B = Node("B", 7, ["A"], ["D", "E"])
C = Node("C", 3, ["A"], ["E", "F"])
D = Node("D", 6, ["B"], ["G"])
E = Node("E", 12, ["B", "C"], ["G", "H"])
F = Node("F", 4, ["C"], ["H"])
G = Node("G", 1, ["D", "E"], ["I", "J"])
H = Node("H", 14, ["E", "F"], ["J", "K"])
I = Node("I", 5, ["G"], ["L"])
J = Node("J", 10, ["G", "H"], ["L", "M"])
K = Node("K", 9, ["H"], ["M"])
L = Node("L", 11, ["I", "J"], ["N"])
M = Node("M", 8, ["J", "K"], ["N"])
N = Node("N", 2, ["L", "M"], [])

nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N]

nodes = forward_pass(nodes)
nodes = backward_pass(nodes)
nodes = calculate_floats(nodes)
print(", ".join(find_critical_path(nodes)))
display(nodes)