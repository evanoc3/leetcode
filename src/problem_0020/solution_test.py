from unittest import TestCase, main
from solution import Solution


class Problem20SolutionTest(TestCase):
	def test_problem_20_solution_1(self):
		actual = Solution().isValid("()")
		self.assertTrue(actual)

	def test_problem_20_solution_2(self):
		actual = Solution().isValid("()[]{}")
		self.assertTrue(actual)

	def test_problem_20_solution_3(self):
		actual = Solution().isValid("(]")
		self.assertFalse(actual)

	def test_problem_20_solution_4(self):
		actual = Solution().isValid("([)]")
		self.assertFalse(actual)

	def test_problem_20_solution_5(self):
		actual = Solution().isValid("{[]}")
		self.assertTrue(actual)


if __name__ == "__main__":
	main()
