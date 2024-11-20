# Themen
#
# Algorithmen
#  Lineare und Binäre Suche https://geekflare.com/de/python-search-algorithms/

from time import perf_counter
import random

def lineare_suche(zahlenarray, suchzahl):
	array_laenge = len(zahlenarray)
	# Durchlaufe das Array
	for schritt in range(array_laenge):
		# Vergleiche das aktuelle Array-Element mit der Suchzahl
		if zahlenarray[schritt] == suchzahl:
			# Gefunden
			return schritt

	# Die zu suchende Zahl wurde nicht im Array gefunden
	return -1


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
		
		# Vergleiche das aktuelle Array-Element mit der Suchzahl
		if sortiertes_zahlenarray[mitte] == suchzahl:
			# Gefunden
			return schritt
		elif sortiertes_zahlenarray[mitte] < suchzahl:
			# Suche rechts
			start = mitte + 1
		else:
			# Suche links
			ende = mitte - 1
		schritt += 1
	
	return -1


if __name__ == '__main__':
	zahlen = 100
	print('Erzeuge ein grosses unsortiertes Array mit ' + str(zahlen) + ' Zahlen')
	zahlenarray = random.sample(range(zahlen), zahlen)
	if zahlen <= 100:
		print(zahlenarray)
	print()
	
	# Lineare Suche
	suchzahl = random.randint(0, zahlen)
	print('Lineare Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	anzahl_schritte = lineare_suche(zahlenarray, suchzahl)
	if anzahl_schritte!= -1:
		print(suchzahl, 'wurde gefunden in ' + str(anzahl_schritte) + ' Schritten')
	else:
		print(suchzahl, 'wurde nicht gefunden')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	suchzahl = zahlen
	print('Lineare Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	anzahl_schritte = lineare_suche(zahlenarray, suchzahl)
	if anzahl_schritte!= -1:
		print(suchzahl, 'wurde gefunden in ' + str(anzahl_schritte) + ' Schritten')
	else:
		print(suchzahl, 'wurde nicht gefunden')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	# Binaere Suche
	print('Sortiere das Array mit Zahlen')
	sortiertes_zahlenarray = zahlenarray
	sortiertes_zahlenarray.sort()
	if zahlen <= 100:
		print(sortiertes_zahlenarray)
	print()
	
	suchzahl = random.randint(0, zahlen)
	print('Binäre Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	anzahl_schritte = binaere_suche(zahlenarray, suchzahl)
	if anzahl_schritte!= -1:
		print(suchzahl, 'wurde gefunden in ' + str(anzahl_schritte) + ' Schritten')
	else:
		print(suchzahl, 'wurde nicht gefunden')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	suchzahl = zahlen
	print('Binäre Suche nach der Zahl ' + str(suchzahl))
	zeit_start = perf_counter()
	anzahl_schritte = binaere_suche(zahlenarray, suchzahl)
	if anzahl_schritte!= -1:
		print(suchzahl, 'wurde gefunden in ' + str(anzahl_schritte) + ' Schritten')
	else:
		print(suchzahl, 'wurde nicht gefunden')
	zeit_stop = perf_counter()
	print('Stoppuhr: ' + str(zeit_stop - zeit_start))
	print()
	
	print('Loesche das Array mit Zahlen')
