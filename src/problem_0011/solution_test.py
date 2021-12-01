from unittest import TestCase, main
from src.problem_0011.solution import Solution


class Problem11SolutionTest(TestCase):
	def test_problem_11_solution_1(self):
		actual = Solution().maxArea([1,8,6,2,5,4,8,3,7])
		expected = 49
		self.assertEqual(actual, expected, "The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49")

	def test_problem_11_solution_2(self):
		actual = Solution().maxArea([1,1])
		expected = 1
		self.assertEqual(actual, expected)
	
	def test_problem_11_solution_3(self):
		actual = Solution().maxArea([4,3,2,1,4])
		expected = 16
		self.assertEqual(actual, expected)

	def test_problem_11_solution_4(self):
		actual = Solution().maxArea([1,2,1])
		expected = 2
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()
