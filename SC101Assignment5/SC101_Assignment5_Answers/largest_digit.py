"""
File: largest_digit.py
Name: Jay
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
	return find_largest_digit_helper(n, '')


def find_largest_digit_helper(n, largest_digit):
	"""
	:param n: the digit needs to be find the largest digit
	:param largest_digit: store the largest digit
	:return: the largest digit
	"""
	# if n is negative number, change it to positive number
	if n < 0:
		n = -n

	# base case, return the largest digit
	if n == largest_digit:
		return n
	else:
		# compare the second-last digit and last digit
		if (n//10) % 10 < n % 10:
			# if the last digit is the largest, delete second-last digit and store last digit
			return find_largest_digit_helper(n // 100 * 10 + n % 10, n % 10)
		else:
			# if the second-last digit is the largest, delete last digit and store second-last digit
			return find_largest_digit_helper(n // 10, (n//10) % 10)


if __name__ == '__main__':
	main()
