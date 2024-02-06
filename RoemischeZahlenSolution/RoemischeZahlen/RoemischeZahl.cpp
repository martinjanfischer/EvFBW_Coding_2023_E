#include "RoemischeZahl.h"

std::string BerechneRoemischezahl(int arabische_zahl)
{
    std::string Roemischezahl = "";

    // 1000
    while (arabische_zahl >= 1000)
    {
        Roemischezahl += "M";
        arabische_zahl -= 1000;
    }

    // von 100 bis 999
    if (arabische_zahl >= 900)
    {
        Roemischezahl += "CM";
        arabische_zahl -= 900;
    }
    if (arabische_zahl >= 500)
    {
        Roemischezahl += "D";
        arabische_zahl -= 500;
    }
    if (arabische_zahl >= 400)
    {
        Roemischezahl += "CD";
        arabische_zahl -= 400;
    }
    while (arabische_zahl >= 100)
    {
        Roemischezahl += "C";
        arabische_zahl -= 100;
    }

    // von 10 bis 99
    if (arabische_zahl >= 90)
    {
        Roemischezahl += "XC";
        arabische_zahl -= 90;
    }
    if (arabische_zahl >= 50)
    {
        Roemischezahl += "L";
        arabische_zahl -= 50;
    }
    if (arabische_zahl >= 40)
    {
        Roemischezahl += "XL";
        arabische_zahl -= 40;
    }
    while (arabische_zahl >= 10)
    {
        Roemischezahl += "X";
        arabische_zahl -= 10;
    }

    // von 1 bis 9
    if (arabische_zahl >= 9)
    {
        Roemischezahl += "IX";
        arabische_zahl -= 9;
    }
    if (arabische_zahl >= 5)
    {
        Roemischezahl += "V";
        arabische_zahl -= 5;
    }
    if (arabische_zahl >= 4)
    {
        Roemischezahl += "IV";
        arabische_zahl -= 4;
    }
    while (arabische_zahl >= 1)
    {
        Roemischezahl += "I";
        arabische_zahl -= 1;
    }

    return Roemischezahl;

}
