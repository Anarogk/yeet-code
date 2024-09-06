# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = temp = ListNode(0, head)
        s = set(nums)
        while head:
            if head.val in s:
                temp.next = head.next
                head.next = None
                head = temp.next
            else:
                temp = head
                head = head.next
        return new_node.next         
                
                