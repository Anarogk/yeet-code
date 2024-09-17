# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # node1, node2 = list1, list2
        # res = node3 = ListNode(0, None)

        # while node1 and node2:
        #     if node1.val <= node2.val:
        #         node3.next = node1
        #         node1 = node1.next
        #     else:
        #         node3.next = node2
        #         node2 = node2.next
        #     node3 = node3.next
        # if node1 and not node2:
        #     node3.next = node1
        # elif node2 and not node1:
        #     node3.next = node2

        # return res.next

        list3 = new = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
        if list1 and not list2:
            list3.next = list1
        elif list2 and not list1:
            list3.next = list2
        return new.next
