#include <iostream>
#include <string>
using namespace std;

void main()
{
	int currentProd1, currentProd2, currentProd = 0;
	for (int i = 999; i > 0; i--)
	{
		for (int j = 999; j > 0; j--)
		{
			string prod = to_string(i * j);
			if (prod.length() % 2 == 0)
			{
				int brk = (prod.length() / 2) * -1;
				for (int low = 0, high = prod.length() - 1; low < high; low++, high--)
					if (prod[high] == prod[low])
						brk++;
				if (brk == 0 && (i * j) > currentProd)
				{
					currentProd = i * j;
					currentProd1 = i;
					currentProd2 = j;
				}
				
			}
		}
	}
	cout << "Winner found: " << currentProd << "Products: " << currentProd1 << ", " << currentProd2;
	system("pause");
}