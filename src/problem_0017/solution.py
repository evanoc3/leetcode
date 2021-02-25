from typing import List
import itertools


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		length = len(digits)
		letter_map = {
			"2": ["a", "b", "c"],
			"3": ["d", "e", "f"],
			"4": ["g", "h", "i"],
			"5": ["j", "k", "l"],
			"6": ["m", "n", "o"],
			"7": ["p", "q", "r", "s"],
			"8": ["t", "u", "v"],
			"9": ["w", "x", "y", "z"]
		}
		if length == 0:
			return []
		elif length == 1:
			return letter_map[digits]
		else:
			letter_permutations = map(lambda digit: letter_map[digit], digits)
			solutions = itertools.product( *letter_permutations )
			solutions = map(lambda tup: "".join(tup), solutions)
			return list(solutions)