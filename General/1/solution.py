# Takes an array of integers as the input
# Outputs the element that is repeated the most
def main(arr):
	myDict = dict()
	for i in arr:
		myDict[i] = myDict.get(i,0) + 1
	arrMax = max(myDict, key=myDict.get)
	print(arrMax)

if __name__ == '__main__':
	arr = [8, 5, 9, 5, 2, 2, 2, 5, 5]
	main(arr)