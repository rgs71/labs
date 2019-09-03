# Die Collatz-Folge

Die [Collatz](https://de.wikipedia.org/wiki/Collatz-Problem)-Folge (auch `3n+1`-Folge genannt), wurde von deutschen Mathematiker Lothat Collatz aufgestellt.

Dabei bildet man die Zahlen der Folge durch folgende Konstruktionsvorschrift:

- Beginne mit irgendeiner natürlichen Zahl `n > 0`.
- Ist `n` gerade, so nimm als nächstes `n/2`.
- Ist `n` ungerade, so nimm als nächstes `3 * n + 1`.
- Wiederhole die Vorgehensweise mit der erhaltenen Zahl, bis die Zahl 1 ist.

## Beispiel

Man startet mit `n = 10`. Da `n` gerade ist, erhält man als nächste 5.
Da 5 ungerade ist, erhält man damit `3 * 5 + 1 = 16`.
Da 16 gerade ist, erhält man 8.
Da 8 gerade ist, erhält man 4.
Da 4 gerade ist, erhält man 2.
Da 2 gerade ist, erhält man 1.

Also ist die Folge
`10 => 5 => 16 => 8 => 4 => 2 =>1`.

## Aufgabe

- Bestimme analog für die Zahl 6 und 13 die zugehörige Folgen.

{% next %}
# Umsetzung mit Python

Um ein Pythonprogramm zu schreiben, welches das Collatz-Problem löst, werden wir schrittweise arbeiten. Dabei erstellen wir zunächst ein Programm, welches ein ähnliches Problem *löst* und modifizeiren dieses so, dass es am Ende das tatsächliche Problem löst. Am Besten speichert man die Zwischenergebnisse mit `git`.

{% next %}
# Halbieren von Zahlen

Zunächst ignorieren wir, dass die Zahlen der Collatz-Folge auch durch die `3 * n +1` vorschrift größer werden können und schreiben ein Programm, welches nur Zahlen halbiert.

1. Dafür schreiben wir zunächst `n = 8` um die Startzahl 8 festzulegen.

1. Da wir abhängig von der Startzahl unterschiedlich viele Schritte bis zum Ende machen, müssen wir eine Wiederholung mit `while`verwenden.

1. Der Konstruktionsvorschrift entnehmen wir, dass wir die Wiederholung abbrechen können, falls wir 1 erreichen.

1. In jedem Schritt der Wiederholung, wird die Zahl, die unter `n`gespeichert ist halbiert.


Das führt uns zu folgendem Programmcode:

```python
n = 8
while n > 1:
    print(n)
    n = n / 2
```

## Aufgabe

- Schreibe den Code in die Datei `collatz.py`.
- Führe das Programm im Terminal aus, indem Du `python collatz.py` schreibst und bestätigst (`ENTER`).
- Notiere die Zahlen, die das Programm ausgibt.
- Was fällt dir bei den ausgegebenen Zahlen auf?
- Änder im Code den Wert von `n` und lasse auch dann das Programm laufen.

