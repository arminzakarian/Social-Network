file_path = 'email-Eu-core.txt'
N = 1005

def count_node_edges(file_path):
    nodes = set()
    edges = 0

    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            nodes.add(sender)
            nodes.add(receiver)
            edges += 1

    num_nodes = len(nodes)
    return num_nodes, edges

num_nodes, num_edges = count_node_edges(file_path)
print('Problem 1 and 2 Results:')
print('>> Number of Nodes: ', num_nodes)
print('>> Number of Edges: ', num_edges)

