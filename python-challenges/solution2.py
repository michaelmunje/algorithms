# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Solution: Use a for loop to multiply all numbers together up to the designed number

# function printFactorial
# Takes an integer a
# Outputs the factorial of that number
def printFactorial(a):
	factorial = 1
	for i in range(1,a + 1):
		factorial *= i
	print(factorial)

if __name__ == '__main__':
	a = 8
	printFactorial(a)