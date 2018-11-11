# General Problem 7:
# Implement binary search of a sorted array of integers

# Solution:
# Binary search algorithm
# 3 functions:
# recursion, specifically divide and conquer recursion
# while loop that uses divide and conquer
# while loop that doesn't use start and end, uses divide and conquer

import math

def binarySearchRec(arr, start, end, value):
	if (start <= end):
		mp = (start + end) // 2
		if (arr[mp] == value):
			return mp
		elif (arr[mp] < value):
			getBin = binarySearchRec(arr, mp + 1, end, value)
			if (getBin != -1):
				return getBin
			else:
				return -1
		else:
			getBin = binarySearchRec(arr, start, mp - 1, value)
			if (getBin != -1):
				return getBin
			else:
				return -1
	return -1

def binarySearchEasy(arr, value):
	end = len(arr) - 1
	start = 0
	while (start <= end):
		mp = (start + end) // 2
		if (arr[mp] == value):
			return mp
		elif (arr[mp] < value):
			start = mp + 1
		else:
			end = mp - 1
	return -1

def binarySearchComplicated(arr, value):
	currentIndex = len(arr) // 2
	numIterations = 0
	currLength = len(arr)
	while(currLength > 0):
		if (arr[currentIndex] == value):
			return currentIndex
		elif (arr[currentIndex] < value):
			if (currLength == 2):
				if (arr[currentIndex + 1] == value):
					return currentIndex + 1
			currentIndex += currLength // 2 // 2
			if (((currLength // 2) % 2) == 0):
				currentIndex += 1
		else:
			if (currLength == 2):
				if (arr[currentIndex - 1] == value):
					return currentIndex - 1
			currentIndex -= currLength // 2 // 2
			if (((currLength // 2) % 2) == 0):
				currentIndex -= 1

		currLength = currLength // 2
	return -1

if __name__ == '__main__':
	arr = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
	val = 3
	#index = binarySearchComplicated(arr, val)
	index = binarySearchRec(arr, 0, len(arr)-1, val)
	if (index != -1):
		print(index)
	else:
		print("Not found.")
