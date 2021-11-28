from typing import List


# Definition for singly-linked list.

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Utility Methods for working with linked Lists

def create_listnode(inputs: List[int]) -> ListNode:
	head=None
	if len(inputs):
		cur = ListNode(val=inputs[0], next=None)
		head = cur
		for i in range(1, len(inputs)):
			cur.next = ListNode(val=inputs[i], next=None)
			cur = cur.next
	return head

def serialize_list(head: ListNode) -> List[int]:
	output = []
	while head != None:
		output.append(head.val)
		head = head.next
	return output


class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		return
	
	def get_best_list_head(self, lists: list[ListNode]) -> ListNode:
		pass
		

        