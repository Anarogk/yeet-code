# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # created None
        curr = head # curr to head

        while curr:
            temp = curr.next # temp for holding next
            curr.next = prev # we set curr's next to prev one
            prev = curr # we move prev pointer to curr 
            curr = temp # we move curr to next pointer
        return prev   