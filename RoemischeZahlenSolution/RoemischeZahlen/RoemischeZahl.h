#pragma once
#include <string>

std::string BerechneRoemischezahl(int arabische_zahl);

class RoemischeZahl
{
public:
    RoemischeZahl(int arabische_zahl)
        : meineArabischeZahl(arabische_zahl)
    {
        meineRoemischeZahl = BerechneRoemischezahl(arabische_zahl);
    }
    int meineArabischeZahl = 0;
    std::string meineRoemischeZahl;
};
