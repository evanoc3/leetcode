from unittest import TestCase, main
from solution import Solution


class Problem3SolutionTest(TestCase):
	def test_problem_3_solution_1(self):
		actual = Solution().lengthOfLongestSubstring("abcabcbb")
		expected = 3
		self.assertEqual(actual, expected, "The answer is \"abc\", with the length of 3")
	
	def test_problem_3_solution_2(self):
		actual = Solution().lengthOfLongestSubstring("bbbbb")
		expected = 1
		self.assertEqual(actual, expected, "The answer is \"b\", with the length of 1")
	
	def test_problem_3_solution_3(self):
		actual = Solution().lengthOfLongestSubstring("pwwkew")
		expected = 3
		self.assertEqual(actual, expected, "The answer is \"wke\", with the length of 3")

	def test_problem_3_solution_4(self):
		actual = Solution().lengthOfLongestSubstring("")
		expected = 0
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()