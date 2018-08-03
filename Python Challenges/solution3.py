# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Solution: Use a for loop to add each entry equal to its square
# then print the dictionary

# function createSquareDict
# Takes an integer a
# Outputs a dictionary containing 1...n entries where the values are the squares of the entry number
def createSquareDict(a):
	squareDict = dict()
	for i in range(1, a + 1):
		squareDict[i] = i*i
	return squareDict

if __name__ == '__main__':
	a = 8
	myDict = createSquareDict(a)
	print(myDict)
