from unittest import TestCase, main
from src.problem_0019.solution import Solution


class Problem19SolutionTest(TestCase):
	def test_problem_19_solution_1(self):
		actual = Solution().removeNthFromEnd(Solution.create_listnode([1,2,3,4,5]), 2)
		expected = [1,2,3,5]
		self.assertEqual(Solution.serialize_list(actual), expected)

	def test_problem_19_solution_2(self):
		actual = Solution().removeNthFromEnd(Solution.create_listnode([1]), 1)
		expected = []
		self.assertEqual(Solution.serialize_list(actual), expected)

	def test_problem_19_solution_3(self):
		actual = Solution().removeNthFromEnd(Solution.create_listnode([1,2]), 1)
		expected = [1]
		self.assertEqual(Solution.serialize_list(actual), expected)


if __name__ == "__main__":
	main()
