from unittest import TestCase, main
from src.problem_0014.solution import Solution


class Problem14SolutionTest(TestCase):
	def test_problem_14_solution_1(self):
		actual = Solution().longestCommonPrefix(["flower","flow","flight"])
		expected = "fl"
		self.assertEqual(actual, expected)

	def test_problem_14_solution_2(self):
		actual = Solution().longestCommonPrefix(["dog","racecar","car"])
		expected = ""
		self.assertEqual(actual, expected, "There is no common prefix among the input strings")


if __name__ == "__main__":
	main()
