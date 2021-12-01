import unittest
from src.problem_0026.solution import Solution


class Problem26SolutionTest(unittest.TestCase):
	def test_problem_26_solution_1(self):
		test_input = [1, 1, 2]
		return_code = Solution().removeDuplicates(test_input)
		self.assertEqual(return_code, 2)
		actual = test_input[:return_code]
		self.assertListEqual([1, 2], actual)

	def test_problem_26_solution_2(self):
		test_input = [0,0,1,1,1,2,2,3,3,4]
		return_code = Solution().removeDuplicates(test_input)
		self.assertEqual(return_code, 5)
		actual = test_input[:return_code]
		self.assertListEqual([0,1,2,3,4], actual)


if __name__ == "__main__":
	unittest.main()