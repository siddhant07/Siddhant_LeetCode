#DFS (Depth-First Search) on a tree (specifically a preorder traversal).

# Represent the family tree as an adjacency list from parent to children

# Store the king’s name as the root of the inheritance tree

# Maintain a set of deceased people for quick lookup

# On birth, append the child to the parent’s children list

# On death, mark the person as dead without removing them from the tree

# Generate inheritance order using DFS starting from the king

# Add a person to the result only if they are not dead

# Traverse children in birth order to preserve inheritance rules

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.nation = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.nation[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []
        self.dfs(self.king)
        return self.ans
    
    def dfs(self, cur):
        if cur not in self.dead:
            self.ans.append(cur)
        for child in self.nation[cur]:
            self.dfs(child)
        
# birth: O(1) (append child)

# death: O(1) (set insert)

# getInheritanceOrder: O(N)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()