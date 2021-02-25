class Solution():
	def lengthOfLongestSubstring(self, s: str) -> int:
		longest = 0
		for cur in range( len(s) ):
			substring = []
			substring.append( s[cur] ) 
			for next_digit in range(cur+1, len(s)):
				if s[next_digit] not in substring:
					substring.append( s[next_digit] )
				else:
					break # break the loop for efficiency
			if len(substring) > longest: longest = len(substring)
		return longest