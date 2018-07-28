# General Problem 9:
# Find the most frequent integer in an array

# Solution: Store the array into a dictionary while counting the occurences
# Store the array into a dictionary while counting the occurences
# Then print out max value in dictionary

# function printMaxCount
# Takes an array of integers as the input
# Outputs the element that is repeated the most
def printPrimesBruteForce(numOfPrimes):
	primes = list()
	for i in range(2, numOfPrimes):
		isPrime = True
		for j in range(2, i):
			if (i % j == 0):
				isPrime = False
		if (isPrime == True):
			primes.insert(len(primes),i)
	print(primes)

if __name__ == '__main__':
	x = 30
	printPrimesBruteForce(x)