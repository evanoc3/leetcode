class Solution:
  def reverse(self, x: int) -> int:
    pos_num = True if (x >= 0) else False # Decide whether to put a plus at the start of the string
    str_int = str(x) if pos_num else str(x)[1:] # skip the first digit ("-") if it's a negative number
    str_int = str_int[::-1] if pos_num else ("-" + str_int[::-1]) # Reverse it, and re-add the "-" if you took it out
    ret = int(str_int)
    if -(2**31) < ret < 2**31-1: # Regular handling
      return ret
    else:
      return 0