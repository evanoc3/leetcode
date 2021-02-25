# Definition for singly-linked list.

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		i = 0
		while l1 or l2:
			if (l1 != None) and (l2 == None or l1.val < l2.val):
				newval = l1.val
				l1 = l1.next
			else:
				newval = l2.val
				l2 = l2.next
			
			if i == 0:
				head = ListNode(val=newval)
				cur = head
			else:
				cur.next = ListNode(val=newval)
				cur = cur.next
			i += 1
		return None if i == 0 else head