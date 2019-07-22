# Schaltjahre

Für einige Situationen ist es wichtig zu wissen, ob ein Jahr ein Schaltjahr ist, um z.B. entscheiden zu können, ob das entsprechende Jahr 365 oder 366 Tage lang war.
Im Folgenden werden wir eine Pythonfunktion schreiben, die entscheidet, ob ein Jahr ein Schaltjahr ist. Dazu müssen wir in der Datei `leapyear.py`einige Ergänzungen in der Funktion `is_leapyear` machen.

{% next 1. Division in Python %}

Rufe zunächst im Terminal `python`auf um ins REPL (read-evaluate-print-loop) zu kommen. Führe dort für verschiedene Zahlen Aufgaben wie
`16 / 4`, `25 // 4`und `27 % 8` aus. Welche der Divisionen verrät uns am ehesten was wir für Schaltjahre wissen müssen?


{% spoiler %}
Nicht gucken! Der Operator `%` gibt uns den Rest bei Divisionen an, wenn dieser 0 ist, geht die Divisionsaufgabe glatt auf und wir wissen die Zahl ist ein Teiler.
{% endspoiler %}
