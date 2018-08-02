# General Problem 9:
# Find the most frequent integer in an array

# Solution: Store the array into a dictionary while counting the occurences
# Store the array into a dictionary while counting the occurences
# Then print out max value in dictionary

# function printMaxCount
# Takes an array of integers as the input
# Outputs the element that is repeated the most
# takes 0.6 s for 5000
def printPrimesBruteForce(numOfPrimes):
	primes = list()
	for i in range(2, numOfPrimes + 1):
		isPrime = True
		for j in range(2, i):
			if (i % j == 0):
				isPrime = False
		if (isPrime == True):
			primes.insert(len(primes),i)
	print(primes)
	print(len(primes))

# takes 0.0 s for 5000
def printPrimesBetter(numOfPrimes):
	primes = [True] * (numOfPrimes + 1)
	for i in range(2, numOfPrimes + 1):
		for j in range(2, ((numOfPrimes + 1) // i) + 1):
				if (i * j <= 5000):
					primes[i * j] = False
	primesList = list()
	for i in range(2, numOfPrimes + 1):
		if (primes[i]):
			primesList.insert(len(primes),i)
	print(primesList)
	print(len(primesList))

if __name__ == '__main__':
	x = 5000
	printPrimesBruteForce(x)
	printPrimesBetter(x)