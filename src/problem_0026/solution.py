class Solution:
	def removeDuplicates(self, nums: list[int]) -> int:
		sort_cursor = 0
		for i in range(1, len(nums)):
			last_sorted_value = nums[sort_cursor]

			if nums[i] > last_sorted_value:
				sort_cursor += 1
				nums[sort_cursor] = nums[i]
		return sort_cursor + 1
		


        