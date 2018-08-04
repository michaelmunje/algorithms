# General Problem 10:
# Write a function that prints out the binary form of an int

# Solution:
# Divide by 2 and see if the current number is a multiple of 2
# Repeat until the num is equal to 0
# Reverse the string and return it

import math

def changeBase(inputInt, base):
	outputString = ""
	currentNum = inputInt
	if (base == 1):
		logEnd = 1
		print("Error. Log(1) = 1. Not a valid base.")
	else:
		logEnd = int(math.log(inputInt, base)) + 1
	for i in range(0, logEnd):
		outputString = outputString + str(currentNum % base)
		currentNum = currentNum // base
	outputString = outputString[::-1]
	return outputString

def intToBin(inputInt):
	outputString = ""
	currentNum = inputInt
	for i in range(0, int(math.log(inputInt, 2)) + 1):
		if (currentNum % 2 == 0):
			outputString = outputString + "0"
		else:
			outputString = outputString + "1"
		currentNum = currentNum // 2
	outputString = outputString[::-1]
	return outputString

if __name__ == '__main__':
	inputInt = 4097
	base = 11
	outputString = changeBase(inputInt, base)
	print(outputString)