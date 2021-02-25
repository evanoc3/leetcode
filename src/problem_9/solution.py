from math import ceil


class Solution:
  def isPalindrome(self, x: int) -> bool:
    try:
      int_str = str(x)
    except:
      raise ValueError
    for a in range( ceil(len(int_str) / 2) ):
      z = len(int_str) - 1 - a
      if not int_str[a] == int_str[z]:
        return False
    return True