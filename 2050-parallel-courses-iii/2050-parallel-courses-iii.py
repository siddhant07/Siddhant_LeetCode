#topological sort with Kahn's algorithm

# Build 0-indexed graph and indegree array

# Initialize queue and maxTime array

# Push indegree-0 nodes into queue and set their maxTime

# Process nodes with Kahn’s algorithm while updating maxTime

# Push neighbors when their indegree becomes 0

# Return the maximum value in maxTime


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n
        
        for (x, y) in relations:
            graph[x - 1].append(y - 1)
            indegree[y - 1] += 1
        
        queue = deque()
        max_time = [0] * n
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                max_time[node] = time[node]

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max(max_time)

#Given e as the length of relations -> O(n+e)