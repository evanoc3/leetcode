from unittest import TestCase, main
from .solution import Solution


class Problem6SolutionTest(TestCase):
	def test_problem_6_solution_1(self):
		actual = Solution().convert("PAYPALISHIRING", 3)
		expected = "PAHNAPLSIIGYIR"
		self.assertEqual(actual, expected)

	def test_problem_6_solution_2(self):
		actual = Solution().convert("PAYPALISHIRING", 4)
		expected = "PINALSIGYAHRPI"
		self.assertEqual(actual, expected, "P     I    N\nA   L S  I G\nY A   H R\nP     I\n")
	
	def test_problem_6_solution_3(self):
		actual = Solution().convert("A", 1)
		expected = "A"
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()
