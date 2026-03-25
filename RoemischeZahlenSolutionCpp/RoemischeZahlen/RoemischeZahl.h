#pragma once
#include <string>

std::string BerechneRoemischezahl(int arabische_zahl);

class RoemischeZahl
{
public:
    RoemischeZahl(int arabische_zahl);
    void print() const;
    RoemischeZahl operator+ (const RoemischeZahl& rechts);
private:
    int meineArabischeZahl = 0;
    std::string meineRoemischeZahl;
};
