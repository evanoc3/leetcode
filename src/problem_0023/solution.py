from typing import Optional


# Definition for singly-linked list.

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Utility methods for linked lists

def create_linked_list(inputs: list[int]) -> ListNode:
	head = None
	if len(inputs):
		cur = ListNode(val=inputs[0], next=None)
		head = cur
		for i in range(1, len(inputs)):
			cur.next = ListNode(val=inputs[i], next=None)
			cur = cur.next
	return head


def serialize_list(head: ListNode) -> list[int]:
	output = []
	while head != None:
		output.append(head.val)
		head = head.next
	return output



class Solution:
	def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
		return
        