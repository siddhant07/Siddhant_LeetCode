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
        