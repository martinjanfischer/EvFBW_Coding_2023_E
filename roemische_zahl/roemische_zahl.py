def berechne_roemische_zahl(arabische_zahl):
    roemische_zahl=""


    while arabische_zahl>=1000:
        arabische_zahl -= 1000
        roemische_zahl += "M"

    # Zahlen 100 bis 999

    if arabische_zahl>=900:
        roemische_zahl+="CM"
        arabische_zahl -= 900

    if arabische_zahl>=500:
        arabische_zahl -= 500
        roemische_zahl+="D"
    if arabische_zahl>=400:
        arabische_zahl -= 400
        roemische_zahl+="CD"

    while arabische_zahl>=100:
        arabische_zahl -= 100
        roemische_zahl += "C"

    # Zahlen 10 bis 99
    if arabische_zahl>=90:
        roemische_zahl+="XC"
        arabische_zahl -= 90

    if arabische_zahl>=50:
        arabische_zahl -= 50
        roemische_zahl+="L"
    if arabische_zahl>=40:
        arabische_zahl -= 40
        roemische_zahl+="XL"

    while arabische_zahl>=10:
        arabische_zahl -= 10
        roemische_zahl += "X"

    # Zahlen 1 bis 9
    if arabische_zahl>=9:
        roemische_zahl+="IX"
        arabische_zahl -= 9

    if arabische_zahl>=5:
        arabische_zahl -= 5
        roemische_zahl+="V"
    if arabische_zahl>=4:
        arabische_zahl -= 4
        roemische_zahl+="IV"

    while arabische_zahl>=1:
        arabische_zahl -= 1
        roemische_zahl += "I"

    return roemische_zahl


if __name__ == '__main__':      # Definiere die __main__ Funktion
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer natürlichen Arabischen Zahl')
    parser.add_argument('arabische_zahl', type=int, help='Eine natürliche Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "berechne_roemische_zahl" 
    # wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    roemische_zahl = berechne_roemische_zahl(args.arabische_zahl)
    print(roemische_zahl)
