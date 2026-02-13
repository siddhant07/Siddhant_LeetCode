# Intuition (2 points)

# It’s a shortest-path problem with a hard limit on number of edges (stops), so we can’t use plain Dijkstra (it optimizes cost, not stops).

# Do BFS by “levels” (each level = +1 stop) and keep best-known costs to prune worse paths within the stop limit.

# Algorithm

# Build an adjacency list from flights

# Initialize cost[] = inf, set cost[src] = 0

# Push (src, 0, 0) into a queue as (node, currCost, stops)

# While queue not empty: pop a state

# If stops > k, continue (don’t expand)

# For each neighbor: compute newCost = currCost + price

# If newCost < cost[neighbor], update cost[neighbor] and push (neighbor, newCost, stops+1)

# Return cost[dst] if reachable, else -1

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        min_cost = [float('inf')] * n
        min_cost[src] = 0
        
        queue = collections.deque([(0, src, 0)]) # (stops, node, cost)
        
        while queue:
            stops, u, cost = queue.popleft()
            if stops > k: continue
            
            for v, w in adj[u]:
                if cost + w < min_cost[v]:
                    min_cost[v] = cost + w
                    queue.append((stops + 1, v, min_cost[v]))
                    
        return min_cost[dst] if min_cost[dst] != float('inf') else -1

# Time complexity: O(K * E) — In the worst case, we explore each edge up to times as we relax the paths.