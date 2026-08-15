# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        if not root.left and not root.right:
            return [root.val]
        q = deque([root])
        res = []
        res.append(root.val)
        while q:
            temp = []
            k = len(q)
            for _ in range(k):
                front = q.popleft()
                if front.left!=None:
                    q.append(front.left)
                    temp.append(front.left.val)
                if front.right!=None:
                    q.append(front.right)
                    temp.append(front.right.val)
            if len(temp)>=1:
                res.append((sum(temp))/(len(temp)))
        return res