# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def isPalindrome(self, head):

        #node의 값들을 deque자료형에 추가
        node_dq = deque()
        node, node_dq = head, deque()
        while node is not None:
            node_dq.append(node.val)
            node = node.next
        
        #팰린드롬 판별
        while len(node_dq) > 1:
            if node_dq.popleft() != node_dq.pop():
                return False
        return True
