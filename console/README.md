# Arbeiten mit der CS50 Sandbox

Hier lernst Du den Umgang mit der CS50 Sandbox/Lab, die wir in Zukunft als Programmierumgebung, die für alle exakt gleich ist, nutzen wollen, damit die kleinen Unterschiede bei Betriebssystem oder den verwendenten Programmen nicht zu Störungen führen.

Das System bietet gleichzeitig eine graphischen Umgebung (*GUI* graphical user interface) sowie ein textbasierte Umgebung (*CLI* command-line interface) mit der man Dateien und Verzeichnisse erstellen und manipulieren kann. Statt des Begriffs CLI wird auch von Kommandozeile, Konsole oder Terminal gesprochen.

Viele Systeme lassen sich nur per Terminal steuern, da auf diese Weise leichter durch Fernzugriff auf z.B. Internetservern o.ä. gearbeitet werden kann. Daher sind grundlegende Kenntnisse des Terminals hilfreich. 

Die verschiedenen Betriebssysteme haben oft leicht unterschiedliche Implementationen ihres Terminals. Hier auf diesem virtualisierten Ubuntu-System lernst Du einiges über das Linux-Terminal. Wenn man z.b. [Cmder](https//:www.cmder.net) verwendet, ist es auch unter Windows möglich die gleichen Befehle zu nutzen - zustätzlich versteht Cmder aber auch windowseigene Befehle. 

> **Beachte** Das Terminal unter Linux unterscheidet Groß- und Kleinschreibung!

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

Viele Betriebssysteme kennen verborgene Verzeichnisse und Dateien, die im Normalfall für Anwender uninteressant sind und daher ausgeblendet werden. Diese können im Terminal mit `ls -a` (**l**i**s**t **a**ll) angezeigt werden.

## Aufgabe
+ Worin unterscheiden sich Ordner und Dateien im Terminal?
+ Überprüfe, ob es versteckte Verzeichnisse oder Dateien gibt? Falls ja, kannst Du vermuten was darin gespeichert wird?

{% next %}
# Verzeichnisse wechseln mit dem GUI

Um den aktuellen Ordner zu wechseln kann man in der GUI mit der Maus einen entsprechdnen Ordner auswählen. Wählt man das Verzeichnis `Buch`, so kann man über das Drei-Punkte-Menü am Verzeichnis Dateien und Unterverzeichnisse erstellen.

## Aufgabe
Erzeuge das Unterverzeichnis `Titelei`(Teile eines Buchs wie Vorwort, Inhaltsverzeichnis, etc.) im Verzeichnis `Buch`.

{% next %}
# Verzeichnisse wechseln mit dem CLI

Im Terminal kann man in einen Unterordner wechseln, indem man den Befehl `cd`(**c**hange **d**irectory) verwendet.  Um also in den Unterordner `Buch`zu wechseln, würde man `cd Buch` verwenden.
Das Terminal kennt auch Abkürzungen für den aktuellen Ordner `.` und für den übergeorneten Ordner `..` - mit diesem kann man dann auch entsprechend aus einem Ordner herauswechseln, indem man `cd ..` (wechsele in den übergeordneten Ordner) benutzt.    

Da man leicht den Überblick verlieren kann gibt der Befehl `pwd` (**p**rint **w**orking **d**irectory) den vollständigen Pfad zum aktuellen Verzeichnis aus.

## Aufgabe
+ Wechsele in das Verzeichnis `Buch` und erzeuge das Unterverzeichnis `Anhang`.
+ Benutze `ls` einmal im Verzeichnis `Buch` und einmal im übergeordnetem Verzeichnis. Was fällt Dir auf?
+ Überprüfe mit `pwd` jeweils das Verzeichnis in dem Du gerade den `ls` Befehl ausführst.

{% next %}
# Dateien kopieren mit dem GUI

Aus Dateiexplorer kennst Du normalerweise die Möglichkeit Dateien und Ordner per *drag and drop* zu verschieben. Dies ist hier leider nicht möglich, da der Browser vermutet man würde die grafischen Elemente greifen wollen.

{% next %}
# Dateien kopieren mit dem CLI

Im Terminal gibt uns die Befehl `cp`(**c**o**p**y) und `mv` (**m**o**v**e) die Möglichkeit Dateien zu kopieren oder zu verschieben. Dabei muss man allerdings den Pfad im Verzeichnisbaum mit angeben. Dabei kann man entweder relativ zum aktuellen Ordner oder relativ zum sogenannten `root`- Verzeichnis die Pfade angeben. Angenommen wir befinden uns im Terminal im Verzeichnis Buch. Dann würde der Befehl `cp ../Vorwort.txt Titelei/Vorwort.txt` die Datei `Vorwort.txt` aus dem übergeordentem Ordner in das Verzeichnis Titelei kopieren. Alternativ kann man auch vollständige Pfadangaben benutzen (diese werden angezeigt, wenn man im GUI mit der Maus auf der Datei ist) durch `mv /root/sandbox/Copyright.txt /root/sandbox/Buch/Anhang/Copyright.txt` entsprechend die Textdatei `Copyrigt.txt` in das Unterverzeichnis `Anhang` verschieben.

## Aufgabe
Führe die beiden Befehle durch, während in dem GUI alle Ordner *geöffnet* sind, so dass Du Unterordner und Dateien innerhalb der Ordner sehen kannst.

{% next %}
# Dateien und Verzeichnisse löschen mit dem GUI

Das Drei-Punkte-Menü neben jeder Datei und jedem Ordner erlaubt es diese zu löschen. Wenn man ein Verzeichnis löscht, wird auch sofort der gesamte Inhalt - also alle Dateien und Unterverzeichnisse -  mitgelöscht.

## Aufgabe 
Lösche den Ordner `Bilder` mit dem GUI.

{% next %}
# Dateien löschen mit dem CLI
 
 Mit dem Kommando `rm` (**r**e**m**ove) kann man eine Datei entfernen. Dabei muss wieder der Pfad angegeben werden. Wenn wir uns im Ordner `Buch` befinden, würde das Kommando `rm ../Vorwort.txt` die Datei `Vorwort.txt`aus dem übergeordentem Verzeichnis löschen. Alternativ könnte man wieder den vollständigen Pfad angeben `rm /root/sandbox/Vorwort.txt`.

## Aufgabe
Lösche jetzt mit dem obigen Befehl die entsprechende Datei.

{% next %}
# Ordner löschen mit dem CLI

 Das Kommando `rmdir` (**r**e**m**ove **dir**ectory) erlaubt es leere Ordner zu löschen. Will man ein ähnliches Verhalten wie in der GUI haben, nutzt man `rm -d -R` (wobei `-d` anzeigt, dass ein Verzeichnis gelöscht werden soll und `-R` anzeigt, dass rekursiv auch alles innerhalb gelöscht werden soll). Allerdings wird man dann auch beim löschen jeder Datei einzeln gefragt und muss den Löschvorgang mit `y` bzw. `yes` bestätigen oder mit `n` bzw. `no` abbrechen.


> Der nächste Abschnitt ist für den Umgang mit dem Terminal sehr nützlich, aber auch entsprechend komplexer!

{% next %}
# Inhalt von Dateien im GUI anzeigen und manipulieren

 Wir haben oben bereits gesehen, dass für die meisten Dateien sofort in der GUI ein Tab geöffnet wird. In diesem Fenster kann man einfach direkt schreiben und so z.B. eine Textdatei verändern. Gleichzeitig sieht man immer den Inhalt der entsprechdenden Datei.

## Aufgabe
+ Erstelle im Ordner `Titelei` eine Textdatei `Inhaltsverzeichnis.txt`.
+ Ergänze in der ersten Zeile den Text `Einleitung`. Die Änderungen werden in der Sandbox automatisch gespeichert - später in der IDE muss man selbst Änderungen speichern.

{% next %}
# Inhalt von Dateien im CLI anzeigen

Zum Anzeigen des Inhalts einer Datei kann man im Terminal den Befehl `cat` (con**cat**enate) benutzen. Mit `cat README.txt` würde also der Inhalt der Datei `README.txt` ausgegeben werden.

## Aufgabe
+ Lasse Dir den Inhalt von `Inhaltsverzeichnis.txt` ausgeben.
+ Was passiert, falls man eine leere Datei wie `Vorwort.txt` anzeigen läßt?
+ Was passiert, wenn man eine nicht 
vorhandene Datei anzeigen lassen will?

{% next %}
# Andere Befehle im CLI

Der Befehl `date` gibt Datum und Uhrzeit des Rechners aus.

Mit dem Befehl `echo` kann man Nachrichten im Terminal anzeigen lassen. Dies ist später hilfreich, wenn man komplexere Vorgänge hat und an bestimmten stellen Ausgaben für den Benutze anzeigen will.

Der Befehl `echo "Test des Befehls echo!" würde entsprechend die Nachricht in den Anführungszeichen ausgeben.

Es gibt auch den Befehl `wc` (**w**ord **c**ount), der unter anderem die Anzahl von Worten zählen kann.

Der Befehl `wc README.txt` würde entsprechende Informationen über `README.txt` anzeigen.





## Aufgabe
+ Überprüfe, ob `date` die gewünschte Information bereitstellt.
+ Benutze `echo` um eine Nachricht wie "Starting download ..." im Terminal anzeigen zu lassen.
+ Erstelle eine Textdatei `README.txt`. Ergänze in einigen Zeilen kurze Sätze wie *Der Hund rennt im Garten*.
+ Benutze `wc README.txt` und interpretiere die Ausgabe. Ändere `README.txt` um diese Vermutungen zu bestätigen.


{% next %}
# Dateien im CLI mit `>` verändern

um ggf. später aus diesen Einträgen Fehler zu erkennen. Man nennt so etwas eine Logdatei.

Möchte man z.B. speichern, zu welcher  Uhrzeit etwas passiert ist könnte `date > Zugriff.log` die Ausgabe von `ls` in `Zugriff.log` speichern. 

## Aufgabe
+ Führe den Befehl `date > Zugriff.log` aus. Öffne dann im Editor diese Logdatei.
+ Führe jetzt noch einmal den gleichen Befehl aus. Was fällt auf?
+ Ersetze beim dritten ausführen `>` durch `>>`. Was ändert sich?
+ Benutze `echo "Inhalt:" >> Zugriff.log`. 
+ Führe jetzt `ls >> Zugriff.log` aus.

{% next %}
# Befehlen mit `<` Dateien zuführen

Wir kennen bereits den Befehl `wc` der Zeilen, Worte und Buchstaben von Textdateien zählen kann.
Die Option `-l` sorgt dafür, dass nur die Anzahl der Zeilen (lines) ausgegeben wird. Damit würde `wc -l Zugriff.log` die Anzahl der Zugriffe auf eine Datei anzeigen können, wenn jedes Mal per `date` bei Änderungen der Zugriff geloggt wird.

Mit `wc -l < Zugriff.log` sendet man den Inhalt von `Zugriff.log` an `wc`. 

## Aufgabe
Lege eine entsprechende Datei `Zugriff.log` an und führe den Befehl aus.

{% next %}
# Befehle mit einander Verketten (`|`)

Will man die Ausgabe eines Befehls einem anderen Befehl als Eingabe mitgeben, könnte man dies über eine entsprechden Datei zwischenspeichern. Einfacher ist es die Befehle direkt zu verketten, dabei wir bei `command1 | command2` die Ausgabe von  `command1` als Eingabe für `command2` genommen.

Möchte man in einem Verzeichnis die Dateien zählen, könnte man mittels `ls` eine Liste der Dateien erzeugen, durch `|` kann man diese direkt an `wc -l` übergeben, so dass nur die Anzahl der Zeilen, welche der Anzahl der Dateien entspricht ausgegeben wird.

## Aufgabe
+ Führe den Befehl `ls | wc -l` in unterschiedlichen Ordnern aus.
+ Überlege Dir, wie Du mit `wc -m` (zählt die Zeichen inklusive Zeilenumbruch) benutzen kannst, um die Anzahl der Buchstaben, die der obere Befehl ausgibt in der Datei `result.txt`zu speichern.

{% spoiler "Lösung" %}
`ls | wc -l | wc -m > result.txt`
{% endspoiler %}