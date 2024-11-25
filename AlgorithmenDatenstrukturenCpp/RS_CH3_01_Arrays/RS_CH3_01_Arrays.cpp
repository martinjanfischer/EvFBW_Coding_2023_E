#include <iostream>

using namespace std;

const int N = 1000;

void main()
{
	int a[N + 1];
	a[1] = 0;

	for (int i = 2; i <= N; i++)
		a[i] = 1;

	for (int i = 2; i <= N / 2; i++)
		for (int j = 2; j <= N / i; j++)
			a[i * j] = 0;

	for (int i = 1; i <= N; i++)
		if (a[i])
			cout << i << ' ';

	cout << endl;
}
