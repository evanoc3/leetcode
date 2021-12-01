from unittest import TestCase, main
from typing import List
from src.problem_0002.solution import ListNode, Solution


# Utility functions for converting between List and ListNode

def create_listnode(list: List) -> ListNode:
	if len(list) > 0:
		return ListNode(val=list[0], next=create_listnode(list[1:]))
	return None


def create_list(ln: ListNode) -> List:
	list = []
	while ln != None:
		list.append(ln.val)
		ln = ln.next
	return list



class Problem2SolutionTest(TestCase):
	def test_problem_2_solution_1(self):
		l1 = create_listnode([2,4,3])
		l2 = create_listnode([5,6,4])
		actual = Solution().addTwoNumbers(l1, l2)
		expected = create_listnode([7,0,8])
		self.assertEqual(create_list(actual), create_list(expected))

	def test_problem_2_solution_2(self):
		l1 = create_listnode([0])
		l2 = create_listnode([0])
		actual = Solution().addTwoNumbers(l1, l2)
		expected = create_listnode([0])
		self.assertEqual(create_list(actual), create_list(expected))

	def test_problem_2_solution_3(self):
		l1 = create_listnode([9,9,9,9,9,9,9])
		l2 = create_listnode([9,9,9,9])
		actual = Solution().addTwoNumbers(l1, l2)
		expected = create_listnode([8,9,9,9,0,0,0,1])
		self.assertEqual(create_list(actual), create_list(expected))


if __name__ == "__main__":
	main()
