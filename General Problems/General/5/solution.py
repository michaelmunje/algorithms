# General Problem 1:
# Find the most frequent integer in an array

# Solution:
# Store the array into a dictionary while counting the occurences
# Then print out max value in dictionary

# function printMaxCount
# Takes an array of integers as the input
# Outputs the element that is repeated the most
def printMinCount(arr):
	myDict = dict()
	for i in arr:
		myDict[i] = myDict.get(i,0) + 1
	arrMax = min(myDict, key=myDict.get)
	lengthOne = list()
	for key, value in myDict.items():
    	  if (value == 1):
    	  	lengthOne.insert(len(lengthOne),key)
	if (len(lengthOne) == 1):
		print(arrMax)
	else:
		print("There is not exactly one element that occurs once.")

if __name__ == '__main__':
	arr = [2, 5, 8, 5, 2, 2, 2, 5, 5]
	printMinCount(arr)
