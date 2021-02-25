from typing import List


# Definition for singly-linked list.

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		serialized = self.serialize_list(head)
		del(serialized[-n])
		return self.create_listnode(serialized)

	@staticmethod
	def create_listnode(inputs: List[int]) -> ListNode:
		head=None
		if len(inputs):
			cur = ListNode(val=inputs[0], next=None)
			head = cur
			for i in range(1, len(inputs)):
				cur.next = ListNode(val=inputs[i], next=None)
				cur = cur.next
		return head

	@staticmethod
	def serialize_list(head: ListNode) -> List[int]:
		output = []
		while head != None:
			output.append(head.val)
			head = head.next
		return output