class Solution:
	def convert(self, s: str, numRows: int) -> str:
		rows = [ "" ] * numRows # Create a 2d list for each row
		currentRow, zig_up = 0, True
		for c in s: # for character in string
			rows[currentRow] += c # Append the letter to the appropriate 
			if numRows > 1: # Don't flip when there's only one row
				currentRow = (currentRow + 1) if (zig_up) else (currentRow - 1) # Increment the row counter depending on the direction
			if (currentRow == numRows - 1) or (currentRow == 0): zig_up = not zig_up # Check for if we should flip the direction
		out_str = ""
		for row in rows: # Add each row together
			out_str += row
		return out_str
