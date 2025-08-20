# Last updated: 8/21/2025, 2:34:27 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1, num2 = [], [] 
        head = ListNode(0)
        dummy = head
        
        while True:
            num1.append(str(l1.val))
            if l1.next == None:
                break
            l1 = l1.next
        
        while True:
            num2.append(str(l2.val))
            if l2.next == None:
                break
            l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        num1 = int("".join(num1))
        num2 = int("".join(num2))

        num1 = str(num1+num2)[::-1]

        for x in num1:
            head.next = ListNode(int(x))
            head = head.next
        head.next = None

        return dummy.next
