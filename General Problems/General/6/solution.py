# General Problem 6:
# Find the common elements of 2 int arrays

# Solution:
# Store the first array into a dictionary 
# Go through second array and determine the values in common

# function printCommonValues
# Takes two arrays
# Prints a list of values in common from the two arrays
def printCommonValues(arr, arr2):
	commonDict = dict()
	commonList = list()
	for i in arr:
		commonDict[i] = 1
	for i in arr2:
		if (commonDict.get(i) != None):
			if (commonDict[i] == 1):
				commonDict[i] = 2
				commonList.insert(len(commonList),i)
	print(commonList)

if __name__ == '__main__':
	arr = [2, 5, 8, 5, 2, 2, 2, 5, 5, 9]
	arr2 = [1, 5, 9, 2]
	printCommonValues(arr, arr2)