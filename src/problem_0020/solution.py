class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) == 0:
			return True
		else:
			ROUND = 0
			SQUARE = 1
			CURLY = 2
			tree = []

			for c in s:
				if c == "(":
					tree.append( ROUND )
				elif c == ")":
					if not tree or tree.pop() != ROUND:
						return False
				elif c == "{":
					tree.append( CURLY )
				elif c == "}":
					if not tree or tree.pop() != CURLY:
						return False
				elif c == "[":
					tree.append( SQUARE )
				elif c == "]":
					if not tree or tree.pop() != SQUARE:
						return False
				else:
					return False
			return not tree