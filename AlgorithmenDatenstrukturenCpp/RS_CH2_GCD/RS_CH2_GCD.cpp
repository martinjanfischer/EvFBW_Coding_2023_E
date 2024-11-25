#include <iostream>

using namespace std;

int gcd(int u, int v, int& anzahl_schritte)
{
	anzahl_schritte = 0;
	while (u > 0)
	{
		if (u < v) { int t = u; u = v; v = t; }
		u = u - v;
		anzahl_schritte += 1;
	}
	return v;
}

int gcd_modulo(int u, int v, int& anzahl_schritte)
{
	anzahl_schritte = 0;
	while (u > 0)
	{
		if (u < v) { int t = u; u = v; v = t; }
		u = u % v;
		anzahl_schritte += 1;
	}
	return v;
}

void main()
{
	int u = 0;
	cout << "u: ";
	cin >> u;
	cout << endl;

	int v = 0;
	cout << "v: ";
	cin >> v;

	if (u > 0 && v > 0)
	{
		int teiler, anzahl_schritte;
		anzahl_schritte = 0;
		teiler = gcd(u, v, anzahl_schritte);
		cout << u << ' ' << v << ' ' << teiler << ' ' << anzahl_schritte << endl;

		anzahl_schritte = 0;
		teiler = gcd_modulo(u, v, anzahl_schritte);
		cout << u << ' ' << v << ' ' << teiler << ' ' << anzahl_schritte << endl;
	}
}
