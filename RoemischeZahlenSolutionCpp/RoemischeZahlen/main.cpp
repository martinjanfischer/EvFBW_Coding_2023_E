#include <iostream>
#include <sstream>
#include "RoemischeZahl.h"

int main(int Argc, char* argv[])
{
	std::cout << "Berechene Römische Zahl aus einer arabischen zahl" << std::endl;
	if (Argc > 1)
	{
		std::stringstream sargument1{ argv[1] };
		int arabische_zahl = 0;
		sargument1 >> arabische_zahl;
		if (!sargument1.fail())
		{
			RoemischeZahl roemische_zahl(arabische_zahl);
			std::cout << roemische_zahl.meineArabischeZahl << std::endl;
			std::cout << roemische_zahl.meineRoemischeZahl << std::endl;
		}
	}
	return 0;
}