# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            second_n = head.next
            head.next = second_n.next #head의 다음 다음을 가르키도록 연결
            second_n.next = head #두번째 노드가 첫번째 노드를 가르키도록 연결
            
            #이전 노드들이 두번째 노드를 가르키도록 연결
            prev.next = second_n
            
            #다음 노드들을 swap하기 위해 head와 prev이동
            #head는 이미 두번째 노드로 이동했으므로 한번만 next하면 다음번에 swap할 첫번째 노드가 됨
            head = head.next
            prev = prev.next.next

        return root.next
