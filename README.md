# EvFBW_Python_2023
Python Programmierkurs 2023 für Jugendliche beim Evangelischen Familienbildungswerk

## Software
Wir arbeiten auf Windows 10 und Windows 11 Computern und installieren dort
- das __Python__ Übersetzer Programm in der __Version 3.11__ von
[www.python.org](https://www.python.org/downloads/release/python-3110/)
- das Textbearbeitungs Programm __Notepad++__ von
[notepad-plus-plus.org](https://notepad-plus-plus.org/downloads/)
- das Bildbearbeitungs Programm __The Gimp__ von
[www.gimp.org](https://www.gimp.org/)
- die Community Version der Entwicklungsumgebung __PyCharm__ von
[www.jetbrains.com](https://www.jetbrains.com/pycharm/download/#section=windows)
- die Audio Software __Audacity__ von
[www.audacityteam.org](https://www.audacityteam.org/download/windows/)

## Zusatz Module
Unsere Python Skripte benötigen zusätzliche Software.
Wir installieren die Module über das Programm Pip.

Um alle in dem Kurs benötigten Module zu installieren
musst Du das folgende Kommando ausführen
```
    pip install -r requirements.txt
```

Um alle in dem Kurs benötigten Module wieder zu deinstallieren
musst Du das folgende Kommando ausführen
```
    pip uninstall -r requirements.txt
```

Ihr könnt jederzeit den Inhalt dieser Datei 
mit allen in dem Kurs aktuell benötigten Modulen ersetzen.
Dazu musst Du das folgende Kommando ausführen
```
    pip freeze > requirements.txt
```

## Römische Zahl aus Arabischer Zahl
Das Programm erwartet ein eine Arabische Zahl als Argument.
1. Wenn keine Arabische Zahl angegeben wird, wird ein Hilfetext angezeigt.
Führe folgendes Kommando aus
```
    python roemische_zahl.py
```
2. Wenn eine Arabische Zahl angegeben wird, wird dafür eine Römische Zahl angezeigt.
Führe folgendes Kommando mit dem Argument 7 aus
```
    python roemische_zahl.py 7
```
3. Das Programm zeigt die Römische Zahl VII an.
```
    VII
```

## Test für Römische Zahl aus Arabischer Zahl
Das Programm testet das eigentliche Programm zur Berechnung der Römischen Zahl.
Dieses Testprogramm ist Euer Sicherheitsnetz und gibt Euch Roten Alarm
wenn das eigentliche Programm fehlerhaft arbeitet.

1. Führe folgendes Kommando aus
```
    python roemische_zahl_test.py
```
2. Wenn alle Tests erfolgreich ausgeführt wurden, erhält man folgende Ausgabe
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
3. Wenn ein oder mehrere Tests fehlgeschlagen sind, erhält man folgende Ausgabe
```
.F
======================================================================
FAIL: teste_roemische_zahl_1_bis_10 (__main__.roemische_zahl_test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Sources\EvFBW_Python_2023\roemische_zahl_test.py", line 30, in teste_roemische_zahl_1_bis_10
    self.assertEqual(ergebnis, 'VIII')       # Melde einen Fehler wenn die Variable ergebnis nicht den Zeichenketten-Text VII enthält
AssertionError: 'VII' != 'VIII'
- VII
+ VIII
?    +


----------------------------------------------------------------------
Ran 2 tests in 0.007s

FAILED (failures=1)
```
