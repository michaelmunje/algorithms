# General Problem 4:
# Write fibbonaci iteratively and recursively (bonus: use dynamic programming)

# Solution:
# Add the basis 1, and 1.
# Then print out max value in dictionary

# function getFibonacciDynamic
# Takes the number of fibonacci
# Outputs the fib. sequence where the length is equal to input

def getFibonacciRecursive(fibIndex,fibonacciRec):
	if (fibIndex > 1):
		currentSum = getFibonacciRecursive(fibIndex - 1, fibonacciRec) + getFibonacciRecursive(fibIndex - 2, fibonacciRec)
	else:
		currentSum = 1
	if (fibIndex >= len(fibonacciRec)):
		fibonacciRec.insert(fibIndex, currentSum)
	print(fibIndex)
	return currentSum

def putFibBasis(fibonacciRec):
	fibonacciRec.insert(0,1)
	fibonacciRec.insert(1,1)

def getFibonacciDynamic(numOfFib,fibonacci):
	if (numOfFib >= 1):
		fibonacci.insert(0,1)
	if (numOfFib >= 2):
		fibonacci.insert(1,1)
	for i in range(0, numOfFib):
			fibonacci.insert(i + 2, fibonacci[i] + fibonacci[i + 1])

if __name__ == '__main__':
	x = 10
	fibonacci = list()
	fibonacciRec = list()
	getFibonacciDynamic(x,fibonacci)
	print(fibonacci)
	putFibBasis(fibonacciRec)
	getFibonacciRecursive(x - 1,fibonacciRec)
	print(fibonacciRec)