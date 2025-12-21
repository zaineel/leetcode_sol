from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        cur = head
        while cur:
            if cur in my_set:
                return True
            else:
                my_set.add(cur)
            cur = cur.next
        return False
    

# 2nd approach
# fast and slow pointers 
    def hasCycleSlowFast(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        