# General Problem 1:
# Find the most frequent integer in an array

# Solution: Store the array into a dictionary while counting the occurences
# Store the array into a dictionary while counting the occurences
# Then print out max value in dictionary

# function printMaxCount
# Takes an array of integers as the input
# Outputs the element that is repeated the most
def printMaxCount(arr):
	myDict = dict()
	for i in arr:
		myDict[i] = myDict.get(i,0) + 1
	arrMax = max(myDict, key=myDict.get)
	print(arrMax)

if __name__ == '__main__':
	arr = [8, 5, 9, 5, 2, 2, 2, 5, 5]
	printMaxCount(arr)