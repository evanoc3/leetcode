numerals = { "M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1 }


class Solution:
  def intToRoman(self, num: int) -> str:
    rom_num = ""
    for k, v in numerals.items():
      while(num >= v):
        rom_num += k
        num -= v
    return rom_num