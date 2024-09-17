# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev , head = None, head
        # while head:
        #     temp = head.next
        #     head.next = prev
        #     prev = head
        #     head = temp

        # return prev

        prev= None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
            