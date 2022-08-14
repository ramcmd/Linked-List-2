# TC: finding mid is O(n) operation, reversing is O(n), and merging is O(n)
# TC: overall, it is O(n)
# SC: since it is in-place, it is O(1) and no auxillary data structure for individual operations

 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.FindMid(head)
        temp = mid.next
        mid.next = None
        
        return self.Merge(head, self.reverse(temp))
    
    
    def FindMid(self, head):
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def Merge(self, headA, headB):
        p1 = headA
        p2 = headB
        
        while p2 != None:
            temp = p1.next
            p1.next= p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp
        
        return headA
    
    
            
        