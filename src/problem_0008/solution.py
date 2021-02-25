INT_MIN, INT_MAX = -(2**31), (2**31-1) # Constant Values, provided in problem


class Solution:
  def myAtoi(self, strn: str) -> int:
    int_found, int_start, int_end = False, -1, -1
    for i in range(len(strn)):
      # Found an int character
      if int_found == False and strn[i] != " ":
        int_found = True
        if strn[i] in ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          int_start = i
        else:
          return 0 # First character found was not a valid character, return 0
      # If the start was found, find the next character that isn't a valid int character, or the end of the string
      elif int_found == True and (not strn[i].isdigit()):
        int_end = i
        break
    # No int found, return 0
    if int_found == False:
      return 0
    # Convert the substring to an int
    substring = strn[int_start : int_end] if (int_end != -1) else strn[int_start:]
    try:
      int_val = int( substring )
    except: 
      return 0
    # Return clauses
    if int_val > INT_MAX:
      return INT_MAX
    elif int_val < INT_MIN:
      return INT_MIN
    else:
      return int_val