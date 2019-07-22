# Schaltjahre

Für einige Situationen ist es wichtig zu wissen, ob ein Jahr ein Schaltjahr ist, um z.B. entscheiden zu können, ob das entsprechende Jahr 365 oder 366 Tage lang war.
Im Folgenden werden wir eine Pythonfunktion schreiben, die entscheidet, ob ein Jahr ein Schaltjahr ist. Dazu müssen wir in der Datei `leapyear.py`einige Ergänzungen in der Funktion `is_leapyear` machen.

{% next "Schritt 1: Informationen sammeln" %}

Finde zunächst heraus, wie ein Schaltjahr definiert ist.
Speichere Deine Erkenntnisse in der Textdatei `pseudocode.txt`.

{% next    "Schritt 2: Pseudocode zu Python" %}

Benutze in der Konsole den Befehl `cp` (copy) um aus der Datei `pseudocode.txt` die Datei `leapyear.py` zu machen. Benutze dafür den Befehl `cp pseudocode.txt leapyear.py`.

Damit es keine Fehler bei Python gibt, ist es außerdem notwenig durch `#`-Symbole vor jede Zeile, diese auszukommentieren.
`# Dies ist ein Kommentar`

{% next "Schritt 3: Funktionsdefinition" %}

Als erstes werden wir in der Datei `leapyear.py` vor allen Kommentaren durch die Zeile `def is_leapyear(year):` die Funktion `is_leapyear` definieren, die beim Aufruf einen Parameter `year` erwartet. Damit die Datei besser lesbar ist, rücken wir die Kommentare um 4 Leerzeichen ein. Am einfachsten gelingt dies, indem man alles markiert und `TAB` drückt. 
Unter allen Kommentaren ergänzen wir noch `return True`, was dafür sorgt, dass unsere Funktion unabhängig vom Parameter `year` immer `True` als Rückgabe wert liefert.

{% spoiler "Codebeispiel" %}
```python
def is_leapyear(year):

    # Die durch 4 ganzzahlig teilbaren Jahre sind Schaltjahre.

    # Säkularjahre, also die Jahre, die ein Jahrhundert abschließen (z. B. 1800, 1900, 2100 und 2200) sind keine Schaltjahre.

    # Schließlich sind die durch 400 ganzzahlig teilbaren Säkularjahre doch Schaltjahre. Damit sind z. B. 1600, 2000 und 2400 jeweils wieder Schaltjahre.

    return True
```
{% endspoiler %}

{% next "Schritt 4: Testen der Funktion"  %}

Rufen wir jetzt im Terminal das Programm über `python main.py` auf, werden wir nach dem Jahr gefragt. Überprüfe, dass unabhängig von Eingabe immer ein Schaltjahr angegeben wird. Dies müssen wir jetzt nach und nach ändern.


{% next "Wiederholung: Division mit Python" %}
Rufe zunächst im Terminal `python`auf um in den REPL (Read-Evaluate-Print-Loop) zu kommen. Führe dort für verschiedene Zahlen Aufgaben wie
`16 / 4`, `25 // 4`und `27 % 8` aus. Welche der Divisionen verrät uns am ehesten, was wir für Schaltjahre wissen müssen?


{% spoiler "Lösung" %}
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


{% next "Schritt 5: Einfache Schaltjahre"  %}

Per Definition kommen Schaltjahre (fast immer) alle vier Jahre vor. Ergänzen Sie an entsprechender Stelle eine geeignte Überprüfung.

{% spoiler "Lösung" %}

```python
def is_leapyear(year):

    # Die durch 4 ganzzahlig teilbaren Jahre sind Schaltjahre.
    # Falls die Jahreszahl nicht durch 4 teilbar ist, kann es kein Schaltjahr sein!
    if year % 4 > 0:
        return False

    # Säkularjahre, also die Jahre, die ein Jahrhundert abschließen (z. B. 1800, 1900, 2100 und 2200) sind keine Schaltjahre.

    # Schließlich sind die durch 400 ganzzahlig teilbaren Säkularjahre doch Schaltjahre. Damit sind z. B. 1600, 2000 und 2400 jeweils wieder Schaltjahre.

    return True
```

{% next "Schritt 6: Testen von einfachen Fällen"  %}

Jetzt sollte mit dem Aufruf von `python main.py` für viele Jahre korrekt angegeben werden, dass es sich *nicht* um Schaltjahre handelt. Allerdings wird für die sogenannten Säkularjahre wie 1900 fälschlicher auch angegeben, dass es Schaltjahre sind.

{% next "Schritt 7: Vervollständigen der anderen Fälle" %}

Durch entsprechende Fallunterscheidungen müssen jetzt noch die anderen Fälle berichtigt werden.

{% spoiler "Lösung" %}
```python
def is_leapyear(year):

    # Die durch 4 ganzzahlig teilbaren Jahre sind Schaltjahre.
    # Falls die Jahreszahl nicht durch 4 teilbar ist, kann es kein Schaltjahr sein!
    if year % 4 > 0:
        return False
    # Jahrezahl ist durch 4 teilbar.
    year //= 4
    # Säkularjahre, also die Jahre, die ein Jahrhundert abschließen (z. B. 1800, 1900, 2100 und 2200) sind keine Schaltjahre.
    # Wenn es ursprünglich kein Säkularjahr war, dann kann man jetzt nicht durch 25 teilen.
    if year % 25 > 0:
        return True
    # Jahreszahl ist doch durch 25 teilbar
    year //= 25

    # Schließlich sind die durch 400 ganzzahlig teilbaren Säkularjahre doch Schaltjahre. Damit sind z. B. 1600, 2000 und 2400 jeweils wieder Schaltjahre.
    # Wenn nicht durch 4 teilbar, ist es kein durch 400 teilbares Jahr
    if year % 4 > 0:
        return False
    # Doch durch 4 und damit durch 400 teilbar

    return True
```
{% endspoiler %}