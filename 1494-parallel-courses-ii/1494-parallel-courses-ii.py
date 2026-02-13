from itertools import combinations 
from collections import defaultdict
import heapq

class Solution:
    def canTakeCourse(self, course_num, graph, taken):
        if course_num in taken:
            return False
        return all(y in taken for y in graph[course_num])

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for x, y in dependencies:
            graph[y].append(x)

        cands = {x for x in range(1, n+1) if x not in graph}
        heap = [(1, frozenset(x)) for x in combinations(cands, min(k, len(cands)))]
        heapq.heapify(heap)

        visited = set()
        while heap:
            semester, taken = heapq.heappop(heap)

            if len(taken) == n:
                return semester

            cands = [x for x in range(1, n+1) if self.canTakeCourse(x, graph, taken)]

            for cand in combinations(cands, min(k, len(cands))):
                new_taken = frozenset(taken.union(cand))
                if (new_taken, semester+1) not in visited:
                    visited.add((new_taken, semester+1))
                    heapq.heappush(heap, (semester+1, new_taken))
        