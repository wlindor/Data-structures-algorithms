# path to file: DFS/Directed-graph/nodes.py
import collections

given_edges = [(1,2), (1,3), (2,4), (4,5), (3,5), (5,6)]
num_of_nodes = 6

def graph_nodes(edges, number_of_nodes):
    adjacency_list = {i: [] for i in range(1, number_of_nodes + 1)}

    for source_node,target_node in edges:
        adjacency_list[source_node].append(target_node)

    return adjacency_list

adjacency_list = graph_nodes(given_edges, num_of_nodes)

def can_visit_all_nodes(adj_list, num_nodes):
    visited_dfs = set()
    visited_stack = set()

    def dfs(node):
        if node not in visited_dfs:
            visited_dfs.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)
        return len(visited_dfs) == num_nodes

    def dfs_stack(node):
        queue = collections.deque()
        queue.append(node)

        while queue:
            cur_node = queue.pop()
            if cur_node not in visited_stack:
                visited_stack.add(cur_node)
                for neighbor in adj_list[cur_node]:
                    queue.append(neighbor)
        return len(visited_stack) == num_nodes

    return (dfs(1))
    return (dfs_stack(1))

print(can_visit_all_nodes(adjacency_list, num_of_nodes))

