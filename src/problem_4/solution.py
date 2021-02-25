from typing import List
from math import floor, ceil


class Solution():
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		merged = merge(nums1, nums2) if len(nums1) >= len(nums2) else merge(nums2, nums1)
		if len(merged) % 2 == 0: # Length is even, get the average
			lower_mid = int(floor( (len(merged)-1) / 2))
			upper_mid = int(ceil( (len(merged)-1) / 2))
			median = median = (merged[lower_mid] + merged[upper_mid]) / 2
		else: # If the merged array has odd length, get the average of the lower and upper mid points
			mid = int((len(merged) - 1) / 2)
			median = merged[mid]
		return median


# Utility method for merging lists

def merge(great: List[int], small: List[int]) -> List[int]:
	for i in small:
		x = 0 # index for 'great' array has to be persistent over the loops
		while x < len(great):
			if i < great[x]: break
			x += 1
		if x == len(great):
			great.append(i)
		else:
			great.insert(x, i)
	return great