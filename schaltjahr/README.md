# Schaltjahre

Für einige Situationen ist es wichtig zu wissen, ob ein Jahr ein Schaltjahr ist, um z.B. entscheiden zu können, ob das entsprechende Jahr 365 oder 366 Tage lang war.
Im Folgenden werden wir eine Pythonfunktion schreiben, die entscheidet, ob ein Jahr ein Schaltjahr ist. Dazu müssen wir in der Datei `leapyear.py`einige Ergänzungen in der Funktion `is_leapyear` machen.

{% next "1. Schritt: Informationen sammeln" %}

Finde zunächst heraus, wie ein Schaltjahr definiert ist.
Speichere Deine Erkenntnisse in der Textdatei `pseudocode.txt`.

{% next    "Pseudocode zu Python" %}

Benutze in der Konsole den Befehl `cp` (copy) um aus der Datei `pseudocode.txt` die Datei `leapyear.py` zu machen. Benutze dafür den Befehl `cp pseudocode.txt leapyear.py`.

Damit es keine Fehler bei Python gibt, ist es außerdem notwenig durch `#`-Symbole vor jede Zeile, diese auszukommentieren.
`# Dies ist ein Kommentar`


{% next " Division mit Python" %}
Rufe zunächst im Terminal `python`auf um in den REPL (Read-Evaluate-Print-Loop) zu kommen. Führe dort für verschiedene Zahlen Aufgaben wie
`16 / 4`, `25 // 4`und `27 % 8` aus. Welche der Divisionen verrät uns am ehesten, was wir für Schaltjahre wissen müssen?


{% spoiler %}
+ Der Operator `/`führt eine *echte* Division aus, dabei wird das Ergebnis auch in einen Dezimalbruch umgewandelt.
```python
>>> 24 / 4
6.0
```

+ Der Operator `//`führt eine sogenannte Ganzzahldivision aus, dabei wird das Ergebnis immer als ganze Zahl ausgegeben.
```python
>>> 25 // 4
6
```

+ Der Operator `%` gibt uns den Rest bei einer Ganzzahldivisionen an.
```python
>>> 26 % 4
2
```

Schaltjahre werden über Aussage der Teilbarkeit definiert. Daher gibt uns `%` am meisten Informationen, da das Ergebnis 0 dafür steht, dass die Division glatt ohne Rest durchgeführt werden konnte, also die Zahl teilbar ist.
```python
>>> 124465 % 11
0
```
D.h. die Zahl 124465 ist durch 11 teilbar. Nachweis liefert dann auch
```python
>>> 124465 / 11
11315.0
>>> 124465 // 11
11315
```
{% endspoiler %}
