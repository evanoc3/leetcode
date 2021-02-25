class Solution:
	def longestPalindrome(self, s: str) -> str:
		lps = s[0]
		for i in range(len(s)):
			for j in range(i, len(s)+1):
				checkstring = s[i:j]
				if Solution.is_palindrome(checkstring):
					if len(checkstring) == len(s):
						return checkstring
					elif len(checkstring) > len(lps):
						lps = checkstring
		return lps
	

	@staticmethod
	def is_palindrome(s: str) -> bool:
		return s == s[::-1]

