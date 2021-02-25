from typing import List


class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    pref = list()
    if len(strs) > 0:
      for i in range(len( min(strs) )):
        letters = list(map(lambda x: x[i], strs))
        if all(x == letters[0] for x in letters):
          pref.append(letters[0])
        else:
          break
      return "".join(pref)
    else:
      return ""