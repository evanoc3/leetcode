from unittest import TestCase, main
from src.problem_0009.solution import Solution


class Problem9SolutionTest(TestCase):
	def test_problem_9_solution_1(self):
		actual = Solution().isPalindrome(121)
		self.assertTrue(actual)

	def test_problem_9_solution_2(self):
		actual = Solution().isPalindrome(-121)
		self.assertFalse(actual, "From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.")
	
	def test_problem_9_solution_3(self):
		actual = Solution().isPalindrome(10)
		self.assertFalse(actual)

	def test_problem_9_solution_4(self):
		actual = Solution().isPalindrome(-101)
		expected = 0
		self.assertFalse(actual)


if __name__ == "__main__":
	main()
