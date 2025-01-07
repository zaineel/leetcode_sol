# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, curr_sum):
            if root is None:
                return False
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum
            
            return has_sum(root.left, curr_sum) or has_sum(root.right, curr_sum)

        return has_sum(root, 0)
        