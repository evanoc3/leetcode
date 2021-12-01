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
		output = []

		while not self.all_empty(lists):
			best_list_index, best_list_val = self.get_best_list_head(lists)
			if best_list_val is None:
				break
			output.append(best_list_val)
			lists[best_list_index] = lists[best_list_index].next

		return create_linked_list(output)
	

	def all_empty(self, lists: list[ListNode]) -> bool:
		return all([x is None for x in lists])
	

	def get_best_list_head(self, lists: list[ListNode]) -> tuple[int, int]:
		best_val = max([x.val for x in lists if x is not None])
		best_i = [x.val for x in lists if x is not None].index(best_val)
		return (best_i, best_val)
        