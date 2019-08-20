# Git

Das Programm Git ist ein Programm zur Dateiversionierung. D.h. es können unterschiedliche Versionen von Dateien  gespeichert werden. Du kennst so etwas vielleicht von einigen Cloudspeicheranbieter, die bestimmte Verzeichnisse und deren Änderungen so speichern, dass so auch ältere Versionen einer Datei zu verfügung stehen.

Im Gegensatz zu solchen Diensten erfordert Git **immer** eine Aktion des Benutzers, da ein automatisches Speichern von Quelltext normalerweise zu nicht lauffähigen Programmen führt. Bei Git ist der Programmierer (Autor) selbst zuständig sein Programm dann zu speichern, wenn es gerade lauffähig ist.

Die Git-Befehle werden normalerweise aus dem Terminal aufgerufen - es gibt aber in vielen Editoren eine Integration von Git.


{% next %}
# Git installieren

Wenn Du auf Deinem eigenem Rechner mit Git arbeiten willst, kannst Du Dir die entsprechdene Version auf der [offiziellen Webseite](https://git-scm.com/) herunterladen. Als gute Alternative gibt es [Cmder](https://www.cmder.net), welcher automatisch eine portable Version von Git installiert. Insbesondere steht auch so auf Windows ein Terminal zur Verfügung, welches zusätzlich die Linux-Befehle kennt.

In Schulen kann es sein, dass die Windowskonsole (`cmd`) aus Sicherheitsgründen gesperrt ist, daher arbeiten wir zunächst im CS50 Lab/Sandbox mit dem Programm Git.

{% next %}
# Überprüfung der Installation

Hier in CS50 Lab kann man im Terminal mit dem Befehl `git --version` die Version von Git anzeigen lassen.

Mit dem entsprechdem Befehl sollte dies auch im Cmder funkionieren.

{% next %}
# Hilfe bei Git

Es ist immer möglich durch `git --help` eine Ausgabe der Hilfe im Terminal zu erzeugen. Jetzt verstehst du vielleicht noch nicht was die Ausgabe bedeutet, aber sobald Du mit Git vertrauter bist, kannst Du Dich so an die entsprechenden Befehle erinnern.


{% next %}
# Git einrichten

Damit man später mit Git sinnvoll arbeiten kann, ist es notwendig einen Benutzer mit Email anzulegen. Sinnvollerweise verwendet man die Daten unter denen man bei Github registriert ist. Die Befehle dafür sind `git config --global user.name "Max Mustermann"` um den Namen global festzulegen. Entsprechend legt `git config --global user.email "max@mustermann.de" die Email-Adresse fest. Ohne den Parameter `--global` kann man innerhalb eines sogenannten Git Repository einen Namen und eine Email festlegen.

Falls nicht standardmäßig eine farbige Terminalausgabe zu erhalten, kann man dies mit `git config color.ui true` aktivieren.

## Aufgaben
+ Lege im Terminal Name und Email fest.
+ Aktiviere die farbige Ausgabe.


{% next %}
# Initialisieren des Git-Repository

Git speichert die Daten in einem sogenanntem Repository (kurz *repo*). Als Repository wird ein Verzeichnis genutzt, deren Unterverzeichnisse und Dateien durch Git gesichert werden sollen.

In unserem Fall werden wir statt mit Quelltext aber zunächst mit reinen Textdateien arbeiten, damit nicht das Programmieren, sondern das Werkzeug Git im Vordergrund steht. Als Beispiel werden wir eine Sammlung von Rezepten anlegen. In den Übungsaufgaben wird entsprechend eine Facharbeit erstellt.

Zunächst legen wir durch `mkdir Rezepte` einen Ordner an und wechseln mit `cd Rezepte` in den Ordner. Als zweites können wir durch `git init` diesen Ordner als Repository initialisieren.

## Aufgabe
+ Lege einen Ordner `Facharbeit` an und wechsele in diesen.
+ Führe `ls -a` aus.
+ Initialisiere jetzt das Git-Repository.
+ Führe noch einmal `ls -a` aus. Was fällt auf? Untersuche!

{% next %}
# Hinzufügen von Dateien

In unserem Rezept Repository werden wir jetzt die Textdatei `Pfannkuchen.txt` anlegen.

Danach führen wir im Terminal (innerhalb des Verzeichnis `Rezepte`) den Befehl `git status` aus.

Git erkennt die neue Datei und schlägt selbst vor, was man evtl. mit dieser Datei machen könnte.

Entsprechden veranlassen wir Git durch `git add Pfannkuchen.txt` die entsprechende Datei zu beobachten und in den sogenannten *Index* aufzunehmen.

Der Befehl `git status` zeigt dies entsprechend an.

Damit das Git Repository diese Datei sichert und nicht nur beobachtet, führen wir `git commit -m "Lasagne.txt erstellt"` aus. Dabei wird durch `-m` angezeigt, dass wir die sogenannten Commit-Message mitgeben - durch diese kann man später leichter Änderungen im Repository nachvollziehen. Der Teil zwischen den Anführungszeichen ist die Nachricht.

## Aufgabe
+ Erstelle in dem Verzeichnis `Facharbeit` die Datei `Literatur.txt`.
+ Füge die Datei  in den Index ein. Überprüfe  den Status des Repositories.
+ Führe einen sogenannten Commit aus - beachte, dass Du dafür Deinen Namen und Deine Email-Adresse über `git config` festgelegt haben.
+ Führe alle drei oberen Schritte auch noch mit einem neuerstellten Ordner `Bilder` durch.

{% next %}
# Die Commit-Historie anzeigen

Wenn man nach einiger Zeit nachvollziehen will, wie sich ein Git Repository verändert hat, kann man mit `git log` eine Auflistung aller Commits anzeigen lassen.

## Aufgabe
+ Betrachte die Commit-Historie für Dein Facharbeit-Repository.
+ Stelle eine Vermutung an, was die entsprechenden Ausgaben bedeuten.

{% next %}
# Commit ID

Du hast sicherlich festgestellt, dass die Logdatei anzeigt, durch welchen User, wann ein Commit durchgeführt wurde. Anhand der Commit-Nachricht hat man auch eine Idee was evtl. passiert ist.

Die erste Zeile beginnt jeweils mit der sogenannten Commit-ID, welche ein SHA-1 Hash ist. Der Wert wird berechnet, aus den vorherigen Commits, dem Autor, seiner Email und den Änderungen an den Dateien. Durch diese ID wird jeder Commit eines Repos eindeutig identifiziert.

Üblicherweise reicht es für viele Git Prozesse aus, nur einen ausreichend langen Anfang der ID zu übermitteln.

## Aufgabe

+ Recherchiere kurz, was eine [Hashfunktion](https://www.inf-schule.de/kommunikation/kryptologie/digitalesignatur/konzept_hashfunktion) ist. Die für Git verwendete Hashfunktion SHA-1 ist aber leider kryptographisch [unsicher](https://www.golem.de/news/hashfunktion-der-schwierige-abschied-von-sha-1-1703-127041.html). 



