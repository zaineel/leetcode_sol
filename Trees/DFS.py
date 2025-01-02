# Depth First Search algorithms
# In DFS, stack is used to store the nodes

# 1. Inorder Traversal
# 2. Preorder Traversal
# 3. Postorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Inorder Traversal

def inorder_traversal(root):
    if not root:
        return []
    
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# 2. Preorder Traversal

def preorder_traversal(root):
    if not root:
        return []
    
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# 3. Postorder Traversal

def postorder_traversal(root):
    if not root:
        return []
    
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]
