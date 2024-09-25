# path to file: DFS/Directed-graph/nodes.py
import collections

class DirectedGraph:
    def __init__(self, edges, num_nodes) -> None:
        self.edges = edges
        self.num_nodes = num_nodes
        self.adjancency_list = {}

    def set_adjancency_list(self) -> dict[int]:
        self.adjancency_list = {i: [] for i in range(1, self.num_nodes + 1)}

        for source_node,target_node in self.edges:
            self.adjancency_list[source_node].append(target_node)

        return self.adjancency_list

    def dfs_recursion(self):
        visited = set()
        node = 1

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in self.adjancency_list[node]:
                    dfs(neighbor)

        dfs(node)
        return len(visited) == self.num_nodes
    
    def dfs_iteration(self):
        queue = collections.deque()
        visited = set()
        node = 1
        queue.append(node)

        while queue:
            cur_node = queue.pop()
            if cur_node not in visited:
                visited.add(cur_node)
                for neighbor in self.adjancency_list[cur_node]:
                    queue.append(neighbor)
        return len(visited) == self.num_nodes
    
given_edges = [(1,2), (1,3), (2,4), (4,5), (3,5), (5,6)]
num_of_nodes = 6
    
graph1 = DirectedGraph(given_edges, num_of_nodes)

graph1.set_adjancency_list()
print(graph1.dfs_recursion())
print(graph1.dfs_iteration())



