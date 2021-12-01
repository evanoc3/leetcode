from unittest import TestCase, main
from src.problem_0007.solution import Solution


class Problem7SolutionTest(TestCase):
	def test_problem_7_solution_1(self):
		actual = Solution().reverse(123)
		expected = 321
		self.assertEqual(actual, expected)

	def test_problem_7_solution_2(self):
		actual = Solution().reverse(-123)
		expected = -321
		self.assertEqual(actual, expected)
	
	def test_problem_7_solution_3(self):
		actual = Solution().reverse(120)
		expected = 21
		self.assertEqual(actual, expected)

	def test_problem_7_solution_4(self):
		actual = Solution().reverse(0)
		expected = 0
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()
