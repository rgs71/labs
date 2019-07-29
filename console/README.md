# Arbeiten mit der CS50 Sandbox

Hier lernst Du den Umgang mit der CS50 Sandbox/Lab, die wir in Zukunft als Programmierumgebung, die für alle exakt gleich ist, nutzen wollen, damit die kleinen Unterschiede bei Betriebssystem oder den verwendenten Programmen nicht zu Störungen führen.

Das System bietet gleichzeitig eine graphsichen Umgebung (*GUI* graphical user interface) sowie ein textbasierte Umgebung (*CLI* command-line interface) mit der man Dateien und Verzeichnisse erstellen und manipulieren kann. Statt des Begriffs CLI wird auch von Kommandozeile oder Terminal gesprochen.

Viele Systeme lassen sich nur per Konsole steuern, da auf diese Weise leichter durch Fernzugriff auf z.B. Internetservern o.ä. gearbeitet werden kann. Grundlegende Kenntnisse von Konsoleneanwendungen sind daher oft hilfreich. 

Die verschiedenen Betriebssysteme haben oft leicht unterschiedliche Implementationen ihrer Konsolenanwendung. Hier auf diesem virtualisierten Ubuntu-System lernst Du einiges über die Linux-Konsole. Wenn man z.b. [Cmder](https//:www.cmder.net) verwendet, ist es auch unter Windows möglich die gleichen Befehle zu nutzen - zustätzlich versteht Cmder aber auch Windows eigene Konsolenbefehle.

{% next %}
# Dateien erstellen mit dem GUI

In dieser  kannst Du Dateien erstellen, indem Du neben dem Ordnersymbol auf das Pluszeichen klickst. Durch eingeben eines Names, erstellst du eine Datei -- Linuxdateien benötigen nicht zwingend eine Dateiendung. Oft gibt es diese aber als Konvention, z.B.  `.pdf` für PDF-Dateien, `.jpg` als Kennzeichen für Bilder im JPEG-Format oder `.txt` für Textdateien.

Danach wird die Datei direkt auch in einem Fenster geöffnet angezeigt. Klickt man das Ordnersymbol an, so ist es möglich den Verzeichnisbaum anzuzeigen.

## Aufgabe
Erstelle eine Datei `Vorwort.txt`.

{% next %}
# Dateien erstellen mit dem  CLI

Das CLI wird hier als Terminal bezeichnet. Oft befindet sich bereits ein geöffnetes Terminal im unteren Bereich. Alternativ kann man in der GUI auch ein Terminal in einem weiterem Fenster öffnen. 

Um eine Datei zu erstellen benutzt man das Kommando `touch`. Dabei wird als Parameter der Dateiname übergeben, d.h. `touch Copyright.txt` würde die Textdatei `Copyright.txt` erstellen. 
Eigentlich aktualisiert `touch` den Zeitstempel der Datei (wann wurde sie das letzte mal angefasst), falls die Datei nicht existiert, wird aber eine neue Datei erstellt.

## Aufgabe
Erstelle die Datei `Copyright.txt` im Terminal.


{% next %}
# Verzeichnisse erstellen mit dem GUI

Um ein Verzeichnis anzulegen, ist es notwendig die Ansicht mit Verzeichnisbaum zu nutzen. Dafür klickt man auf das Ordner-Symbol am oberen Rand. Danach sieht man den Verzeichnisbaum mit allen Ordnern und Dateien. Ein neues Verzeichnis (oder auch eine neue Datei) kann man über das oberste Symbol mit den drei Punkten erstellen.

## Aufgabe
+ Lege einen Ordner `Buch`an.
+ Woran erkennt man, das `Buch` ein Verzeichnis ist?

{% next %}
# Verzeichnisse erstellen mit dem CLI

Im Terminal läßt sich ein Verzeichnis mit dem Kommando `mkdir` (für **m**a**k**e **dir**ectory) kann man Verzeichnisse erstellen. Dabei erzeugt `mkdir Bilder` einen Ordner mit Namen `Bilder`.

## Aufgabe
Erstelle das Verzeichnis `Buch` im Terminal.

{% next %}
# Verzeichnissen anzeigen mit dem CLI

Mit dem Befehl `ls` (**l**i**s**t) kann man sich die Dateien und Unterverzeichnisse in einem Verzeichnis anzeigen lassen. Würden wir jetzt in der Konsole `ls` aufrufen, würden wir die Dateien `Vorwort.txt` und `Copyright.txt`sowie den Ordner `Buch` angezeigt bekommen.

## Aufgabe
Worin unterscheiden sich Ordner und Dateien in der Konsole?

{% next %}
# `mkdir` -- Verzeichnisse in der Konsole erstellen



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
