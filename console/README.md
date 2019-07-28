# Arbeiten mit der CS50 Sandbox

Hier lernst Du den Umgang mit der CS50 Sandbox/Lab, die wir in Zukunft als Programmierumgebung, die für alle exakt gleich ist, nutzen wollen, damit die kleinen Unterschiede bei Betriebssystem oder den verwendenten Programmen nicht zu Störungen führen.

{% next %}
# Dateien erstellen und anzeigen

In dieser Umgebung kannst Du Dateien erstellen, indem Du neben dem Ordnersymbol auf das Pluszeichen klickst. Durch eingeben eines Names, erstellst du eine Datei -- Linuxdateien benötigen nicht zwingend eine Dateiendung. Oft gibt es diese aber als Konvention, z.B.  `.pdf` für PDF-Dateien, `.jpg` als Kennzeichen für Bilder im JPEG-Format oder `.txt` für Textdateien.

Danach wird die Datei direkt auch in einem Fenster geöffnet angezeigt. Klickt man das Ordnersymbol an, so ist es möglich den Verzeichnisbaum anzuzeigen.

## Aufgabe
Erstelle eine Datei `Buch`.

{% next %}
# Verzeichnisse erstellen

Um ein Verzeichnis anzulegen, ist es notwendig die Ansicht mit Verzeichnisbaum zu nutzen. Dafür klickt man auf das Ordner-Symbol am oberen Rand. Danach sieht man den Verzeichnisbaum mit allen Ordnern und Dateien. Ein neues Verzeichnis (oder auch eine neue Datei) kann man über das oberste Symbol mit den drei Punkten erstellen.

## Aufgabe
+ Lege einen Ordner `Buch`an.
+ Woran erkennt man, was die Datei `Buch` und welches der Ordner `Buch`ist?

{% next %}
# Die Konsole

Viele Systeme lassen sich nur per Konsole steuern, da auf diese Weise leichter durch Fernzugriff auf z.B. Internetservern o.ä. gearbeitet werden kann. Grundlegende Kenntnisse von Konsoleneanwendungen sind daher oft hilfreich. 

Die verschiedenen Betriebssysteme haben oft leicht unterschiedliche Implementationen ihrer Konsolenanwendung. Hier auf diesem virtualisierten Ubuntu-System lernst Du einiges über die Linux-Konsole. Wenn man z.b. [Cmder](https//:www.cmder.net) verwendet, ist es auch unter Windows möglich die gleichen Befehle zu nutzen - zustätzlich versteht Cmder aber auch Windows eigene Konsolenbefehle.

{% next %}
# `ls` -- Inhalt von Verzeichnissen anzeigen

Mit dem Befehl `ls` (**l**i**s**t) kann man sich die Dateien in einem Verzeichnis anzeigen lassen. Würden wir jetzt in der Konsole `ls` aufrufen, würden wir die Datei `Buch` und den Ordner `Buch` angezeigt bekommen.

## Aufgabe
Worin unterscheiden sich Ordner und Dateien in der Konsole?


{% next %}
# `mkdir` -- Verzeichnisse in der Konsole erstellen

Mit dem Befehl `mkdir` (für **m**a**k**e **dir**ectory) kann man Verzeichnisse erstellen. Dabei erzeugt `mkdir test` einen Ordner mit Namen Test.

## Aufgabe
Erstelle den Ordner `Rezepte` mit Hilfe der Konsole.

{% spoiler "Lösung" %}
`mkdir Rezepte`
![Befehle für mkdir](sandbox2.gif)
{% endspoiler %}



{% next %}
# `cd` -- Zwischen Verzeichnisse wechseln

In der Konsole kann man in einen Unterordner wechseln, indem man den Befehl `cd`(**c**hange **d**irectory) verwendet.  Um also in den Unterordner `Buch`zu wechseln, würde man `cd Buch` eingeben. Die Linuxkonsole unterscheidet Groß- und Kleinschreibung, d.h. `cd buch` würde gegebenenfalls eine Fehlermeldung produzieren. In der Konsole gibt es auch eine Abkürzung für den aktuellen Ordner `.` und für den übergeorneten Ordner `..` - mit diesem kann man dann auch entsprechend aus einem Ordner herauswechseln, indem man `cd ..` (wechsele in den übergeordneten Ordner) benutzt.    

{% next %}
# `touch` -- Dateien in der Konsole erstellen

Mit dem Befehl `touch test` kannst Du eine Datei erstellen. Unter Linux ist es nicht notwendig, Dateien eine Dateiendung zu geben. 

## Aufgabe

Erstelle jetzt in der Konsole eine Textdatei mit geeignete Namen für ein Rezept Deiner Wahl (z.B. `Lasagne.txt`).

{% spoiler "Lösung" %}
`touch Lasagne.txt`
![Befehle für touch](sandbox4.gif)
{% endspoiler %}

{% next %}
# Dateien ergänzen und anzeigen

Den Inhalt einer Datei kann man im Fenster des Editors ansehen - für jede geöffnete Datei erhält man ein neues Tab. Gleichzeitig erlaubt diese Ansicht auch das Editieren der entsprechenden Datei.

## Aufgabe

Ergänze in jeder Textdatei eine Zeile mit einer Überschrift (z.B. `1. Kapitel`).
