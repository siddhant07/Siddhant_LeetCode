# Use a Trie-like tree where each node represents a directory or file

# Each TrieNode stores:
# - content (only meaningful for files)
# - children map: name -> child node (auto-creates nodes for mkdir/add)
# - isfile flag to distinguish files from directories

# Maintain a single root node `top` as the filesystem starting point

# Helper idea used everywhere:
# - split path by "/"
# - walk from root, skipping empty parts (handles leading "/")

# ls(path):
# - traverse to the node for `path`
# - if it's a file, return [last path component]
# - otherwise return sorted list of child names (directory listing)

# mkdir(path):
# - traverse path and create missing nodes along the way using children[p]

# addContentToFile(filePath, content):
# - traverse to file node, creating missing nodes
# - append content to node.content
# - mark node as a file (isfile = True)

# readContentFromFile(filePath):
# - traverse to file node
# - return node.content

class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = defaultdict(TrieNode)
        self.isfile = False
    
class FileSystem:

    def __init__(self):
        self.top = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans
        
        
    def mkdir(self, path: str) -> None:
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True
    
    def readContentFromFile(self, filePath: str) -> str:
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        return node.content

# (let L = number of path components, K = number of entries in a directory):
# ls(path)
# Total: O(L + K log K)

# mkdir(path)
# Total: O(L)

# addContentToFile(filePath, content)
# Total: O(L + len(content))

# readContentFromFile(filePath)
# Total: O(L)