# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root,isleft):
            global res
            if root is None:
                return 0    
            if not root.left and not root.right and isleft:
                self.res += root.val
                return
            left = solve(root.left,True)
            right = solve(root.right,False)
        
        solve(root,False)
        return self.res