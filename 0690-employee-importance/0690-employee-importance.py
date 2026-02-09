"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}

        q=deque([id])
        ans=0
        
        while q:
            emp_id=q.popleft()
            ans+=emap[emp_id].importance
            
            for sub in emap[emp_id].subordinates:
                q.append(sub)
        return ans
        
        