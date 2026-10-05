# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        left-=1
        right-=1
        
        while right>left:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

        head = ListNode(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return head 
        