# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        for _ in range(right+1):
            last = last.next

        prev_node = dummy
        for _ in range(left-1):
            prev_node = prev_node.next
        curr = prev_node.next
        prev = last
        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        prev_node.next = prev
        return dummy.next
