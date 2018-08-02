# General Problem 2:
# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

# Solution:
# Go through array and calculate the sum of every pair

# function find2SumBruteForce
# takes an input of target sum and the array we want to check
# returns a list of the integer pair if found, otherwise returns an empty list

def find2SumBruteForce(sum, arr):
	twoSum = list()
	for i in arr:
		for j in range(i + 1, len(arr)):
			if (arr[i] + arr[j] == sum):
				twoSum.insert(0,arr[i])
				twoSum.insert(1,arr[j])
				return twoSum
	return twoSum

if __name__ == '__main__':
	arr = [8, 5, 9, 5, 2, 2, 2, 5, 5]
	twosumList = find2SumBruteForce(11,arr)
	print(twosumList)
