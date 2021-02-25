from unittest import TestCase, main
from typing import List
from .solution import Solution, ListNode


# Utility functions for working with Linked Lists

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


class Problem21SolutionTest(TestCase):
	def test_problem_21_solution_1(self):
		l1 = create_listnode([1,2,4])
		l2 = create_listnode([1,3,4])
		actual = Solution().mergeTwoLists(l1, l2)
		expected = [1,1,2,3,4,4]
		self.assertListEqual(serialize_list(actual), expected)

	def test_problem_21_solution_2(self):
		l1 = create_listnode([])
		l2 = create_listnode([])
		actual = Solution().mergeTwoLists(l1, l2)
		expected = []
		self.assertListEqual(serialize_list(actual), expected)

	def test_problem_21_solution_3(self):
		l1 = create_listnode([])
		l2 = create_listnode([0])
		actual = Solution().mergeTwoLists(l1, l2)
		expected = [0]
		self.assertListEqual(serialize_list(actual), expected)


if __name__ == "__main__":
	main()
