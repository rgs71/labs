# Arbeiten mit der CS50 Sandbox

Hier lernst Du den Umgang mit der CS50 Sandbox/Lab, die wir in Zukunft als Programmierumgebung, die für alle exakt gleich ist, nutzen wollen, damit die kleinen Unterschiede bei Betriebssystem oder den verwendenten Programmen nicht zu Störungen führen.

Das System bietet gleichzeitig eine graphsichen Umgebung (*GUI* graphical user interface) sowie ein textbasierte Umgebung (*CLI* command-line interface) mit der man Dateien und Verzeichnisse erstellen und manipulieren kann. Statt des Begriffs CLI wird auch von Kommandozeile oder Terminal gesprochen.

Viele Systeme lassen sich nur per Konsole steuern, da auf diese Weise leichter durch Fernzugriff auf z.B. Internetservern o.ä. gearbeitet werden kann. Grundlegende Kenntnisse von Konsoleneanwendungen sind daher oft hilfreich. 

Die verschiedenen Betriebssysteme haben oft leicht unterschiedliche Implementationen ihrer Konsolenanwendung. Hier auf diesem virtualisierten Ubuntu-System lernst Du einiges über die Linux-Konsole. Wenn man z.b. [Cmder](https//:www.cmder.net) verwendet, ist es auch unter Windows möglich die gleichen Befehle zu nutzen - zustätzlich versteht Cmder aber auch Windows eigene Konsolenbefehle. 

> **Beachte** Die Linuxkonsole unterscheidet Groß- und Kleinschreibung!

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

Mit dem Befehl `ls` (**l**i**s**t) kann man sich die Dateien und Unterverzeichnisse in einem Verzeichnis anzeigen lassen. Würden wir jetzt im Terminal `ls` aufrufen, würden wir die Dateien `Vorwort.txt` und `Copyright.txt`sowie die Ordner `Bilder` und `Buch` angezeigt bekommen.

## Aufgabe
Worin unterscheiden sich Ordner und Dateien in der Konsole?

{% next %}
# Verzeichnisse wechseln mit dem GUI

Um den aktuellen Ordner zu wechseln kann man in der GUI mit der Maus einen entsprechdnen Ordner auswählen. Wählt man das Verzeichnis `Buch`, so kann man über das Drei-Punkte-Menü am Verzeichnis Dateien und Unterverzeichnisse erstellen.

## Aufgabe
Erzeuge das Unterverzeichnis `Titelei`(Teile eines Buchs wie Vorwort, Inhaltsverzeichnis, etc.) im Verzeichnis `Buch`.

{% next %}
# Verzeichnisse wechseln mit dem CLI

Im Terminal kann man in einen Unterordner wechseln, indem man den Befehl `cd`(**c**hange **d**irectory) verwendet.  Um also in den Unterordner `Buch`zu wechseln, würde man `cd Buch` verwenden.
Das Terminal kennt auch Abkürzungen für den aktuellen Ordner `.` und für den übergeorneten Ordner `..` - mit diesem kann man dann auch entsprechend aus einem Ordner herauswechseln, indem man `cd ..` (wechsele in den übergeordneten Ordner) benutzt.    

## Aufgabe
+ Wechsele in das Verzeichnis `Buch` und erzeuge das Unterverzeichnis `Anhang`.
+ Benutze `ls` einmal im Verzeichnis `Buch` und einmal im übergeordnetem Verzeichnis. Was fällt Dir auf?

{% next %}
# Dateien kopieren mit dem GUI

Aus Dateiexplorer kennst Du normalerweise die Möglichkeit Dateien und Ordner per *drag and drop* zu verschieben. Dies ist hier leider nicht möglich, da der Browser vermutet man würde die grafischen Elemente greifen wollen.

{% next %}
# Dateien kopieren mit dem CLI

Im Terminal gibt uns die Befehl `cp`(**c**o**p**y) und `mv` (**m**o**v**e) die Möglichkeit Dateien zu kopieren oder zu verschieben. Dabei muss man allerdings den Pfad im Verzeichnisbaum mit angeben. Dabei kann man entweder relativ zum aktuellen Ordner oder relativ zum sogenannten `root`- Verzeichnis die Pfade angeben. Angenommen wir befinden uns im Terminal im Verzeichnis Buch. Dann würde der Befehl `cp ../Vorwort.txt Titelei/Vorwort.txt` die Datei `Vorwort.txt` aus dem übergeordentem Ordner in das Verzeichnis Titelei kopieren. Alternativ kann man auch vollständige Pfadangaben benutzen (diese werden angezeigt, wenn man im GUI mit der Maus auf der Datei ist) durch `mv /root/sandbox/Copyright.txt /root/sandbox/Buch/Anhang/Copyright.txt` entsprechend die Textdatei `Copyrigt.txt` in das Unterverzeichnis `Anhang` verschieben.

## Aufgabe
+ Führe die beiden Befehle durch, während in dem GUI alle Ornder *geöffnet* sind, so dass Du Unterordner und Dateien innerhlab der Ordner sehen kannst.