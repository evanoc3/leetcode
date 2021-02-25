from unittest import TestCase, main
from .solution import Solution


class Problem1SolutionTest(TestCase):
	def test_problem_1_solution_1(self):
		actual = Solution().twoSum([2,7,11,15], 9)
		expected = [0,1]
		self.assertEqual(actual, expected, "Because nums[0] + nums[1] == 9, we return [0, 1]")

	def test_problem_1_solution_2(self):
		actual = Solution().twoSum([3,2,4], 6)
		expected = [1,2]
		self.assertEqual(actual, expected)

	def test_problem_1_solution_3(self):
		actual = Solution().twoSum([3,3], 6)
		expected = [0,1]
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()