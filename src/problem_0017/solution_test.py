from unittest import TestCase, main
from .solution import Solution


class Problem17SolutionTest(TestCase):
	def test_problem_17_solution_1(self):
		actual = Solution().letterCombinations("23")
		expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
		self.assertListEqual(actual, expected)

	def test_problem_17_solution_2(self):
		actual = Solution().letterCombinations("")
		expected = []
		self.assertListEqual(actual, expected)

	def test_problem_17_solution_3(self):
		actual = Solution().letterCombinations("2")
		expected = ["a","b","c"]
		self.assertListEqual(actual, expected)


if __name__ == "__main__":
	main()
