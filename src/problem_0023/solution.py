from typing import Optional
from sys import maxsize


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


# Solution functions

def all_empty(lists: list[ListNode]):
	# return all([x is None for x in lists])
	for search_list in lists:
		if search_list is not None:
			return False
	return True


def get_next_val(lists: list[ListNode]) -> ListNode:
	best_val = min([ x.val if x is not None else maxsize for x in lists])
	best_i = [x.val if x is not None else maxsize for x in lists].index(best_val)

	lists[best_i] = lists[best_i].next
	
	if lists[best_i] is None:
		del lists[best_i]

	return ListNode(val=best_val)



class Solution:
	def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
		head, tail, new_tail = None, None, None

		while not all_empty(lists):
			new_tail = get_next_val(lists)

			if tail is None:
				tail = new_tail
				continue
			elif head is None:
				head = tail
			
			tail.next = new_tail
			tail = tail.next

		if head is not None:
			return head
		elif new_tail is not None:
			return new_tail
		else:
			return None
        