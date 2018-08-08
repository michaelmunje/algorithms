# General Problem 6:
# Write a function that prints out the binary form of an int

# Solution:

def getExponentBrute(x, y):
	exp = 1
	for i in range(1, y + 1):
		exp *= x
	return exp

def getExponentFast(x, y):
	exp = 1
	if (y % 2 == 1):
		exp *= x
	y2 = y - (y % 2)
	while (y2 > 1):
		y2 = y2 // 2
		if (y2 )
	return exp


if __name__ == '__main__':
	x = 2
	y = 6
	print(getExponentFast(x,y))