from unittest import TestCase, main
from src.problem_0008.solution import Solution


class Problem8SolutionTest(TestCase):
	def test_problem_8_solution_1(self):
		actual = Solution().myAtoi("42")
		expected = 42
		self.assertEqual(actual, expected)

	def test_problem_8_solution_2(self):
		actual = Solution().myAtoi("   -42")
		expected = -42
		self.assertEqual(actual, expected)
	
	def test_problem_8_solution_3(self):
		actual = Solution().myAtoi("4193 with words")
		expected = 4193
		self.assertEqual(actual, expected, "\"4193\" is read in; reading stops because the next character is a non-digit")

	def test_problem_8_solution_4(self):
		actual = Solution().myAtoi("words and 987")
		expected = 0
		self.assertEqual(actual, expected, "The parsed integer is 0 because no digits were read.")

	def test_problem_8_solution_5(self):
		actual = Solution().myAtoi("-91283472332")
		expected = -2147483648
		self.assertEqual(actual, expected, "Since -91283472332 is less than the lower bound of the range [-2^31, 2^31 - 1], the final result is clamped to -2^31 = -2147483648")


if __name__ == "__main__":
	main()
