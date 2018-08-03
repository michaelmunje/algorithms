#include <iostream>

using namespace std;

void main()
{
	int i = 20;
	bool flag = true;
	do
	{
		int counter = 0;
		for (int j = 1; j < 21; j++)
		{
			if (i % j == 0)
				counter++;
		}
		if (counter == 20)
		{
			cout << i;
			system("pause");
		}
		i++;
	} while (flag == true);
}