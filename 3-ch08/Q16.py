# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        #역순 연결리스트 반환
        def reverse_linkedlist(head):
            node, prev = head, None
            while node:
                next, node.next = node.next, prev
                node, prev = next, node
            return prev
        
        #연결리스트를 리스트로 반환
        def to_list(head):
            val_list = []
            node = head
            while node:
                val_list.append(node.val)
                node = node.next
            return val_list
        
        #문자열을 연결리스트로 반환
        def to_linkedlist(str_num):
            head = ListNode(str_num[0])
            node = head
            for i in range(1, len(str_num)):
                node.next = ListNode(str_num[i])
                node = node.next
            
            return head
        
        num1 = int(''.join([ str(n) for n in to_list(reverse_linkedlist(l1))]))
        num2 = int(''.join([ str(n) for n in to_list(reverse_linkedlist(l2))]))
        sum = num1 + num2
        
        return reverse_linkedlist(to_linkedlist(str(sum)))
