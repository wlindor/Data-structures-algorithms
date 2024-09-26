# path to file: DFS/Directed-graph/nodes.py

class DirectedGraph:
    def __init__(self, edges, num_nodes) -> None:
        self.edges = edges
        self.num_nodes = num_nodes
        self.adjacency_list = {}

    def set_adjacency_list(self) -> dict[int, list[int]]:
        self.adjacency_list = {i: [] for i in range(1, self.num_nodes + 1)}

        for source_node,target_node in self.edges:
            self.adjacency_list[source_node].append(target_node)

        return self.adjacency_list

    def dfs_recursion(self):
        visited = set()
        node = 1

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in self.adjacency_list[node]:
                    if neighbor in visited:
                        continue
                    dfs(neighbor)
        dfs(node)
    
        return len(visited) == self.num_nodes
    
    def dfs_iteration(self):
        stack = []
        visited = set()
        node = 1
        stack.append(node)

        while stack:
            cur_node = stack.pop()
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for neighbor in self.adjacency_list[cur_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return len(visited) == self.num_nodes
    
    def has_cycle(self):
        pass
    
given_edges = [(1,2), (1,3), (2,4), (4,5), (3,5), (5,6)]
num_of_nodes = 6
    
graph1 = DirectedGraph(given_edges, num_of_nodes)

graph1.set_adjacency_list()
print(graph1.dfs_recursion())
print(graph1.dfs_iteration())



