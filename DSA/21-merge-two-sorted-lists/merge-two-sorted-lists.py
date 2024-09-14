# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        res = node3 = ListNode(0, None)

        while node1 and node2:
            if node1.val <= node2.val:
                node3.next = node1
                node1 = node1.next
            else:
                node3.next = node2
                node2 = node2.next
            node3 = node3.next
        if node1 and not node2:
            node3.next = node1
        elif node2 and not node1:
            node3.next = node2

        return res.next
