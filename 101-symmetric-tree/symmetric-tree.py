# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def solve(p1,p2):
            if not p1 and not p2:
                return True
            elif not p1:
                return False
            elif not p2:
                return False
            elif p1.val != p2.val:
                return False
            return solve(p1.left,p2.right) and solve(p1.right,p2.left)

        return solve(root.left,root.right)
        