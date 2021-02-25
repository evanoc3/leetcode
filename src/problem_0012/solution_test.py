from unittest import TestCase, main
from .solution import Solution


class Problem12SolutionTest(TestCase):
	def test_problem_12_solution_1(self):
		actual = Solution().intToRoman(3)
		expected = "III"
		self.assertEqual(actual, expected)

	def test_problem_12_solution_2(self):
		actual = Solution().intToRoman(4)
		expected = "IV"
		self.assertEqual(actual, expected)
	
	def test_problem_12_solution_3(self):
		actual = Solution().intToRoman(9)
		expected = "IX"
		self.assertEqual(actual, expected)

	def test_problem_12_solution_4(self):
		actual = Solution().intToRoman(58)
		expected = "LVIII"
		self.assertEqual(actual, expected, "L = 50, V = 5, III = 3")
	
	def test_problem_12_solution_5(self):
		actual = Solution().intToRoman(1994)
		expected = "MCMXCIV"
		self.assertEqual(actual, expected, "M = 1000, CM = 900, XC = 90 and IV = 4")


if __name__ == "__main__":
	main()
