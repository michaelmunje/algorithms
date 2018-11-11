#include <iostream>
using namespace std;
bool isPrime(int);
void main()
{
	int primeCount = 1;
	for (int i = 3; primeCount < 10001 + 1; i += 2)
		if (isPrime(i))
		{
			if (primeCount == 10000)
				cout << "10001st prime: " << i;
			primeCount++;
		}
	system("pause");
}

bool isPrime(int num)
{
	for (int j = 2; j <= sqrt(num); j++)
		if (num % j == 0)
			return false;
	return true;
}