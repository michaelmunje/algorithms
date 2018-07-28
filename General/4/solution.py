# General Problem 4:
# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)

# Solution:
# Add the basis 1, and 1.
# Then print out max value in dictionary

# function listFibonacciDynamic
# Takes the number of fibonacci
# Outputs the sequence where number of integers is equal to input

def listFibonacciRecursive(numOfFib):
	fibonacci = list()
	if (numOfFib >= 1):
		fibonacci.insert(0,1)
	if (numOfFib >= 2):
		fibonacci.insert(1,1)
	for i in range(0, numOfFib):
			fibonacci.insert(i + 2, fibonacci[i] + fibonacci[i + 1])
	return fibonacci

def listFibonacciDynamic(numOfFib):
	fibonacci = list()
	if (numOfFib >= 1):
		fibonacci.insert(0,1)
	if (numOfFib >= 2):
		fibonacci.insert(1,1)
	for i in range(0, numOfFib):
			fibonacci.insert(i + 2, fibonacci[i] + fibonacci[i + 1])
	return fibonacci

if __name__ == '__main__':
	x = 50
	fibonacci = listFibonacci(x)
	print(fibonacci)