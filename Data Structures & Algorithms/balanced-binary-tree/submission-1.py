# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(curr):
            nonlocal balanced
            if curr is None:
                return 0
            
            if abs(dfs(curr.left) - dfs(curr.right)) > 1:
                balanced = False
            if curr.left:
                return dfs(curr.left) + 1
            elif curr.right:
                return dfs(curr.right) + 1
            else:
                return 1    
        dfs(root)
        return balanced

