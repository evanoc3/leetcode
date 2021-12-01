from unittest import TestCase
import unittest
from src.problem_0023.solution import Solution, create_linked_list, serialize_list


class Problem23SolutionTest(unittest.TestCase):
	def test_problem_23_solution_1(self):
		input = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2,6])]
		actual = serialize_list(Solution().mergeKLists(input))
		expected = [1, 1, 2, 3, 4, 4, 5, 6]
		self.assertListEqual(actual, expected)


if __name__ == "__main__":
	unittest.main()