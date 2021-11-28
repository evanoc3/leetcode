from unittest import TestCase, main
from solution import Solution


class Problem4SolutionTest(TestCase):
	def test_problem_4_solution_1(self):
		actual = Solution().findMedianSortedArrays([1,3], [2])
		expected = 2.00000
		self.assertEqual(actual, expected, "merged array = [1,2,3] and median is 2")

	def test_problem_4_solution_2(self):
		actual = Solution().findMedianSortedArrays([1,2], [3,4])
		expected = 2.50000
		self.assertEqual(actual, expected, "merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5")
	
	def test_problem_4_solution_3(self):
		actual = Solution().findMedianSortedArrays([0,0], [0,0])
		expected = 0.00000
		self.assertEqual(actual, expected)
	
	def test_problem_4_solution_4(self):
		actual = Solution().findMedianSortedArrays([], [1])
		expected = 1.00000
		self.assertEqual(actual, expected)

	def test_problem_4_solution_5(self):
		actual = Solution().findMedianSortedArrays([2], [])
		expected = 2.00000
		self.assertEqual(actual, expected)


if __name__ == "__main__":
	main()