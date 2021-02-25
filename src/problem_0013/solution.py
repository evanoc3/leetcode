numerals = { "M":1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1, "": 0 }


class Solution:
  def romanToInt(self, s: str) -> int:
    rom_int = 0
    prev_char = ""
    for c in reversed(s):
      if numerals[c] >= numerals[prev_char]:
        rom_int += numerals[c]
      else:
        rom_int -= numerals[c]
      prev_char = c
    return rom_int