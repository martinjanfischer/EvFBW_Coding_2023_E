#include <iostream>
#include <sstream>
#include "RoemischeZahl.h"

int main(int Argc, char* argv[])
{
	std::cout << "Berechene Roemische Zahl aus einer arabischen zahl" << std::endl;

	if (Argc > 1)
	{
		std::stringstream sargument1{ argv[1] };
		int arabische_zahl = 0;
		sargument1 >> arabische_zahl;
		if (!sargument1.fail())
		{
			RoemischeZahl r(arabische_zahl);
			r.print();
		}
	}
	else
	{
		RoemischeZahl r2(2);			// II
		r2.print();
		RoemischeZahl r3(3);			// III
		r3.print();
		RoemischeZahl rsumme = r2 + r3;	// II + III == V ?
		rsumme.print();

	}

	return 0;
}