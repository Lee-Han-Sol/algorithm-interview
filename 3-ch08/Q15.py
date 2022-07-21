# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        def reverse(node, prev = None):
            if not node: #node = None 일 경우 역순연결리스트(prev)완성 이므로 반환
                return prev
            
            #next에 .next할당 / node.next에 역순연결리스트 완성 된 부분 연결
            next, node.next = node.next, prev
            
            return reverse(next, node)
        
        return reverse(head)
