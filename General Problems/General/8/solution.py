# General Problem 8:
# Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})

# Solution:
# Similar to general 7
# We assume that the rotated array is sorted
# First we find the real starting index of the rotated array
# Then we perform binary search, except we consider the real starting index
# Therefore, we will need to use modulus to get the index correct
# Note: need to keep track of when start passes end to terminate loop

def binarySearchRot(arr, value, startRealIndex):
	end = ((startRealIndex - 1) + len(arr)) % len(arr)
	start = startRealIndex
	startPassedEnd = False
	while (startPassedEnd != True):
		mp = ((( ((start - startRealIndex) % len(arr))  + ( (end - startRealIndex + len(arr)) % len(arr))) // 2) + startRealIndex) % len(arr)
		if (arr[mp] == value):
			return mp 
		elif (arr[mp] < value):
			if ((((start - startRealIndex) % len(arr))  - ( (end - startRealIndex + len(arr)) % len(arr))) == 0 ):
				startPassedEnd = True
			else:
				start = (mp + 1) % len(arr)
		else:
			if ((((start - startRealIndex) % len(arr))  - ( (end - startRealIndex + len(arr)) % len(arr))) == 0 ):
				startPassedEnd = True
			else:
				end = ((mp - 1) + len(arr)) % len(arr)

	return -1

def findStart(arr):
	lastValue = arr[0]
	for i in range(1, len(arr)):
		if (arr[i] < lastValue):
			return i
		lastValue = arr[i]
	return 0

if __name__ == '__main__':
	arr = [8, 9, 10, 0, 1, 3, 4, 5, 6, 7]
	val = 9
	startRealIndex = findStart(arr)
	index = binarySearchRot(arr, val, startRealIndex)
	if (index != -1):
		print(index)
	else:
		print("Not found.")