# Themen
#
# Algorithmen
#  Lineare und Binäre Suche https://geekflare.com/de/python-search-algorithms/

import os
import math
from time import perf_counter
import random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def lineare_suche(zahlenarray, suchzahl):
	array_laenge = len(zahlenarray)
	# Durchlaufe das Array
	schritt = 0
	for schritt in range(array_laenge):
		# Vergleiche das aktuelle Array-Element mit der Suchzahl
		if zahlenarray[schritt] == suchzahl:
			# Gefunden
			return True, schritt+1

	# Die zu suchende Zahl wurde nicht im Array gefunden
	return False, schritt+1


def binaere_suche(sortiertes_zahlenarray, suchzahl):
	# Laenge des Arrays, Start Index und End Index
	array_laenge = len(sortiertes_zahlenarray)
	start = 0
	ende = array_laenge - 1
	mitte = int((start + ende) / 2)

	# Durchlaufe das Array
	schritt = 0
	while schritt < array_laenge and start != mitte and mitte != ende:
		# Berechne den Index der Mitte
		mitte = int((start + ende) / 2)
		schritt += 1
		
		# Vergleiche das aktuelle Array-Element mit der Suchzahl
		if sortiertes_zahlenarray[mitte] == suchzahl:
			# Gefunden
			return True, schritt
		elif sortiertes_zahlenarray[mitte] < suchzahl:
			# Suche rechts
			start = mitte + 1
		else:
			# Suche links
			ende = mitte - 1
	
	return False, schritt


if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	
	zahlen = 128
	print('Erzeuge ein grosses unsortiertes Array mit ' + str(zahlen) + ' Zahlen')
	zahlenarray = random.sample(range(zahlen), zahlen)
	if zahlen <= 128:
		print(zahlenarray)
	print()
	
	# Lineare Suche
	suchzahl = random.randint(0, zahlen-1)
	print('Lineare Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	ergebnis = lineare_suche(zahlenarray, suchzahl)
	if ergebnis[0]==True:
		print(suchzahl, f'wurde {bcolors.OKGREEN}gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	else:
		print(suchzahl, f'wurde {bcolors.FAIL}nicht gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	suchzahl = zahlen
	print('Lineare Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	ergebnis = lineare_suche(zahlenarray, suchzahl)
	if ergebnis[0]==True:
		print(suchzahl, f'wurde {bcolors.OKGREEN}gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	else:
		print(suchzahl, f'wurde {bcolors.FAIL}nicht gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	# Binaere Suche
	print('Sortiere das Array nach aufsteigenden Zahlen')
	sortiertes_zahlenarray = zahlenarray
	sortiertes_zahlenarray.sort()
	if zahlen <= 128:
		print(sortiertes_zahlenarray)
	print()
	
	suchzahl = random.randint(0, zahlen-1)
	print('Binäre Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	ergebnis = binaere_suche(zahlenarray, suchzahl)
	if ergebnis[0]==True:
		print(suchzahl, f'wurde {bcolors.OKGREEN}gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	else:
		print(suchzahl, f'wurde {bcolors.FAIL}nicht gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	suchzahl = zahlen
	print('Binäre Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	ergebnis = binaere_suche(zahlenarray, suchzahl)
	if ergebnis[0]==True:
		print(suchzahl, f'wurde {bcolors.OKGREEN}gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	else:
		print(suchzahl, f'wurde {bcolors.FAIL}nicht gefunden{bcolors.ENDC} nach {bcolors.BOLD}' + str(ergebnis[1]) + f'{bcolors.ENDC} Schritten')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	print('Loesche das Array mit Zahlen')
	print()
	
	print(2**7, 'ist die Zweierpotenz 2**7 also 2 hoch 7')
	print()
	print('Die Hochzahl (also der Exponent)', int(math.log(128,2)), 'zur Basis 2')
	print('lässt sich durch die Logarithmus Funktion math.log(128,2)')
	print('aus dem Wert 128 zur Basis 2 bestimmen')
