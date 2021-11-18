"""
File: largest_digit.py
Name: Sher
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: numbers to be valued
	:return: the largest number
	"""
	largest = 0
	return find_largest_digit_helper(n, largest)


def find_largest_digit_helper(n, largest):
	# let n always > 0
	if n < 0:
		n *= -1
	# base case
	if n < 10:
		if n > largest:
			largest = n
		return largest
		pass
	#  compare digit number by n % 10 and let n //10 do recursion
	else:
		if n % 10 > largest:
			largest = n % 10
		return find_largest_digit_helper(n//10, largest)





if __name__ == '__main__':
	main()
