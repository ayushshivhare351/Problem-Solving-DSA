# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        l1,l2=0,0
        while p1:
            p1=p1.next
            l1 +=1
        while p2:
            p2=p2.next
            l2 +=1
        p1 = headA
        p2 = headB
        while l1>l2:
            p1=p1.next
            l1-=1
        while l2>l1:
            p2=p2.next
            l2-=1
        
        while p1!=p2:
            if p1 is None or p2 is None:
                return None
            p1 = p1.next
            p2 = p2.next
        return p1