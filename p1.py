import math
def is_square(number):
	'''problem 1)
	write a function that tells you if a number is a perfect square
	return True when the variable number is a perfect square
	return False when the variable called number is not a perfect square
	e.g. 
		number=16 -> True 
		number =15 -> False
	'''


	root = math.sqrt(number)
	print root
	if root == 1:
		return True
	else:
		return False


