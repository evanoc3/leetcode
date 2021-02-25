from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for x in range(len(nums)): # Loop over the list
      # For a positive target
      if target >= 0:
        other_num = target - nums[x]
        if(nums[x] == other_num): nums[x] = None # Prevent nums[x] from being the second index picked
        try:
          y = nums.index(other_num)
          return [x, y]
        except ValueError:
          pass
      # For a negative target
      else:
        other_num = target - nums[x]
        try:
          y = nums.index(other_num)
          return [x, y]
        except ValueError:
          pass