# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        count = 0
        curr = head
        while curr!=None:
            curr = curr.next
            count+=1
        n = count//k
        i=0
        while n>0:
            prev_node = dummy
            for _ in range(k*i):
                prev_node = prev_node.next
            i+=1
            curr1 = prev_node.next
            for _ in range(k-1):
                curr1 = curr1.next
            prev = curr1.next
            temp = prev_node.next
            for _ in range(k):
                first = temp.next
                temp.next = prev
                prev = temp
                temp = first
            prev_node.next = prev
            n-=1
        return dummy.next
            