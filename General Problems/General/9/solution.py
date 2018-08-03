# General Problem 9:
# Use dynamic programming to find the first X prime numbers

# Solution: 
# Sieve of Eratosthenes
# Start with a boolean list that represents primality of ints from 2 to numOfPrimes + 1
# For each number from 2 to numOfPrimes, set all of its multiples to false, except for the initial

# function printPrimesBruteForce
# Checks to see if each number has any multiples, if so, it is not prime
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


# function printPrimesBetter
# Uses the sieve of eratosthenes method to compute in linear time as opposed to poly
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