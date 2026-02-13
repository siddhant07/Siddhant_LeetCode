# DSA Used: Graph Theory + DFS / BFS

# Intuition:
# An undirected graph is a tree if and only if it is fully connected and contains no cycles—both of which can be verified using DFS (or BFS).

# Algorithm:

# Build an adjacency list from the edge list

# Run DFS (or BFS) starting from node 0, tracking visited nodes

# Use a parent map (or parameter) to avoid counting trivial back-edges as cycles

# If DFS encounters a visited node that is not the parent, a cycle exists → return false

# After traversal, check if all N nodes were visited (graph is connected)

# Return true if both conditions hold, else false

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        parent = {0: -1}
        queue = collections.deque([0])
        
        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                queue.append(neighbour)
        
        return len(parent) == n

        # Time Complexity : O(N+E).
        