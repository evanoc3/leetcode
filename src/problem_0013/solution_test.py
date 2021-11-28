from unittest import TestCase, main
from solution import Solution


class Problem13SolutionTest(TestCase):
	def test_problem_13_solution_1(self):
		actual = Solution().romanToInt("III")
		expected = 3
		self.assertEqual(actual, expected)

	def test_problem_13_solution_2(self):
		actual = Solution().romanToInt("IV")
		expected = 4
		self.assertEqual(actual, expected)
	
	def test_problem_13_solution_3(self):
		actual = Solution().romanToInt("IX")
		expected = 9
		self.assertEqual(actual, expected)

	def test_problem_13_solution_4(self):
		actual = Solution().romanToInt("LVIII")
		expected = 58
		self.assertEqual(actual, expected, "L = 50, V = 5, III = 3")
	
	def test_problem_13_solution_5(self):
		actual = Solution().romanToInt("MCMXCIV")
		expected = 1994
		self.assertEqual(actual, expected, "M = 1000, CM = 900, XC = 90 and IV = 4")


if __name__ == "__main__":
	main()
