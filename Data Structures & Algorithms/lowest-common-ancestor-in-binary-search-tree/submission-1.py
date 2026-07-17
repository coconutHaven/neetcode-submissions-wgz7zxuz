# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            if curr is None:
                return
            if q.val <= curr.val <= p.val or p.val <= curr.val <= q.val:
                return curr
            elif q.val < curr.val:
                return dfs(curr.left)
            else:
                return dfs(curr.right)
        return dfs(root)
