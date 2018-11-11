# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Solution: For each num in the range of a to b
# If the num is divisible by a and not divisible by b, add to the list
# Then print out the list

# function printDivNotDiv
# Takes a range, a to b. Also takes two divisors, c and d
# The number must divide c but does not divide d
# Outputs each number that satisfies the above property
def printDivNotDiv(a, b, c, d):
	goodNums = list()
	for i in range(a,b):
		if (i % c == 0 and i % d != 0):
			goodNums.insert(len(goodNums), i)	
	print(goodNums)

if __name__ == '__main__':
	a = 2000
	b = 3200
	c = 7
	d = 5
	printDivNotDiv(a, b, c, d)