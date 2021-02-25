from typing import List

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		l1_digits = Solution.transcribeList(l1)
		l2_digits = Solution.transcribeList(l2)
		# Pad lists
		if len(l1_digits) != len(l2_digits):
			bigger = l1_digits if len(l1_digits) > len(l2_digits) else l2_digits
			smaller = l1_digits if len(l1_digits) < len(l2_digits) else l2_digits
			diff = len(bigger) - len(smaller)
			while diff > 0:
				smaller.append(0)
				diff -= 1
		# Begin arithmetic
		result = []
		carry = 0
		for i in range( len(l1_digits) ):
			result_digit = l1_digits[i] + l2_digits[i] + (1 if carry else 0)
			carry = 0
			if result_digit >= 10:
				carry = 1
				result_digit -= 10
			result.append(result_digit)
		if carry: result.append(1)
		return Solution.createList(result)


	@staticmethod
	def transcribeList(l: ListNode) -> List[int]:
		digits = []
		while l.next != None:
			digits.append(l.val)
			l = l.next
		digits.append(l.val)
		return digits


	@staticmethod
	def createList(l: List[int], reverse=True) -> ListNode:
		if reverse: l.reverse()
		old_node = ListNode( l[0] )
		try:
			for i in range( 1, len(l) ):
				new_node = ListNode( l[i] )
				new_node.next = old_node
				old_node = new_node
			return new_node
		except:
			return old_node
