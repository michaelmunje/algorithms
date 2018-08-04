# General Problem 12:
# Implement the square root function

# Solution:
# Use an algorithm that starts off at 0 and increments by a value
# whenever the total is still less than our target
# if we get ahead of the target, instead we lower the increment value
# repeat until our increment value reaches a small enough value,
# this implies our start is close enough to the square root

def guessSquareRoot(inputInteger):
	currentRange = 1
	start = 0
	if (inputInteger >= 1):
		while(currentRange > 0.0001):
			if ((start + currentRange)*(start + currentRange) < inputInteger):
				start = start + currentRange
			else:
				currentRange *= .1
	elif (inputInteger == 0):
		return 0
	else:
		currentRange = .1
		start = 0
		while(currentRange > 0.0001):
			if ((start + currentRange)*(start + currentRange) < inputInteger):
				start = start + currentRange
			else:
				currentRange *= .1
	return start


if __name__ == '__main__':
	inputInteger = 50
	sqrtRoot = guessSquareRoot(inputInteger)
	print(sqrtRoot)