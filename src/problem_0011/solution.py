from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
    max_area, start, end = 0, 0, len(height) - 1
    while start != end:
      cur_area = min([ height[start], height[end] ]) * (end - start)
      if cur_area > max_area:
        max_area = cur_area
      if height[end] > height[start]:
        start += 1
      else:
        end -= 1
    return max_area