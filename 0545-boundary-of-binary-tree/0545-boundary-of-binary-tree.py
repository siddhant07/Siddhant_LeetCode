# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DSA Used: Tree Traversal (DFS & BFS)

# Intuition:
# Traverse the tree in parts—left boundary, leaves, and right boundary—so each boundary node is added once and in the required order.

# Algorithm:
# Traverse the left boundary (excluding leaves) and add nodes to res
# Traverse the tree to collect all leaf nodes and add them to res
# Traverse the right boundary (excluding leaves) in bottom-up order and add nodes to res


from collections import deque
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        
		# bfs
        def left_boundary(node): 
            q = deque([node])
            while q:
                node = q.popleft()
                if node.left is None and node.right is None:
                    return
                res.append(node.val)
                q.append(node.left) if node.left else q.append(node.right)

		# dfs, top-down
        def leaves(node):
            if node.left is None and node.right is None:
                res.append(node.val)
            if node.left:
                leaves(node.left)
            if node.right:
                leaves(node.right)

		# dfs, bottom up
        def right_boundary(node):
            if node.left is None and node.right is None:
                return
            right_boundary(node.right) if node.right else right_boundary(node.left)
            res.append(node.val)

        res = [root.val]
        
        if root.left:
            left_boundary(root.left)
        
        if root.left or root.right:
            leaves(root)

        if root.right:
            right_boundary(root.right)
                
        return res
# Time Complexity: O(n)


        