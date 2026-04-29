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


# Definiere Klasse "RoemischeZahl"
# Wir können Objekte von diesem Typ erzeugen
# und in Variablen speichern
class RoemischeZahl:
    
    # der Konstruktor-Funktion übergeben wir 
    # der Parameter-Variablen "arabische_zahl" 
    # den Anfangswert des RoemischeZahl Objektes, z.B.
    #  r = RoemischeZahl(7)
    #  r.roemische_zahl == 'VII'
    def __init__(self, arabische_zahl):
        if arabische_zahl < 0:
            arabische_zahl = 0
        self.arabische_zahl = arabische_zahl
        self.roemische_zahl = berechne_roemische_zahl(arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte addieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_summe = r_links + r_rechts
    #  r_summe.roemische_zahl == 'XI'
    def __add__(self, rechte_roemische_zahl):
        summe_arabische_zahl = self.arabische_zahl + rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(summe_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte voneinander subtrahieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_differenz = r_links - r_rechts
    #  r_differenz.roemische_zahl == 'III'
    def __sub__(self, rechte_roemische_zahl):
        differenz_arabische_zahl = self.arabische_zahl - rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(differenz_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte multiplizieren, z.B.
    #  r_links = RoemischeZahl(7)
    #  r_rechts = RoemischeZahl(4)
    #  r_produkt = r_links * r_rechts
    #  r_produkt.roemische_zahl == 'XXVIII'
    def __mul__(self, rechte_roemische_zahl):
        produkt_arabische_zahl = self.arabische_zahl * rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(produkt_arabische_zahl)
    
    # Wir können zwei RoemischeZahl Objekte voneinander dividieren, z.B.
    #  r_links = RoemischeZahl(33)
    #  r_rechts = RoemischeZahl(11)
    #  r_quotient = r_links // r_rechts
    #  r_quotient.roemische_zahl == 'III'
    def __floordiv__(self, rechte_roemische_zahl):
        quotient_arabische_zahl = self.arabische_zahl // rechte_roemische_zahl.arabische_zahl
        return RoemischeZahl(quotient_arabische_zahl)
    
    # Wir können ein RoemischeZahl Objekt auf der Kommandozeile ausgeben
    def ausgabe(self):
        print(self.roemische_zahl)


if __name__ == '__main__':      # Definiere die __main__ Funktion
    import argparse
    parser = argparse.ArgumentParser(description = 'Berechne die Römische Zahl aus einer natürlichen Arabischen Zahl')
    parser.add_argument('arabische_zahl', type=int, help='Eine natürliche Arabische Zahl')
    args = parser.parse_args()
    
    # Die obige Funktion "berechne_roemische_zahl" 
    # wird nur dann in der Kommandozeile ausgeführt...
    # ... wenn man sie hier in der __main__ Funktion aufruft
    if True:
        roemische_zahl = RoemischeZahl(args.arabische_zahl)
        roemische_zahl.ausgabe()
    else:
        roemische_zahl = berechne_roemische_zahl(args.arabische_zahl)
        print(roemische_zahl)
