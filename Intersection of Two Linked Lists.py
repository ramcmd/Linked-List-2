# TC: O(m +n) where m and n are the length of the respective linked lists
# SC: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 1
        lenB = 1
        
        p1 = headA
        p2 = headB
        
        while p1.next != None:
            p1 = p1.next
            lenA += 1
        
        while p2.next != None:
            p2 = p2.next
            lenB += 1
        
        p1 = headA
        p2 = headB
        
        if lenA > lenB:
            while lenA != lenB:
                p1 = p1.next
                lenA -= 1
        
        elif lenB > lenA:
            while lenB != lenA:
                p2 = p2.next
                lenB -= 1
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1
            