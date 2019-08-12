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
# Initialisieren des Git-Repository

Git speichert die Daten in einem sogenanntem Repository (kurz *repo*). Als Repository wird ein Verzeichnis genutzt, deren Unterverzeichnisse und Dateien durch Git gesichert werden sollen.

In unserem Fall werden wir statt mit Quelltext aber zunächst mit reinen Textdateien arbeiten, damit nicht das Programmieren, sondern das Werkzeug Git im Vordergrund steht. Als Beispiel werden wir eine Sammlung von Rezepten anlegen. In den Übungsaufgaben wird entsprechend eine Facharbeit erstellt.

Zunächst legen wir durch `mkdir Rezepte` einen Ordner an und wechseln mit `cd Rezepte` in den Ordner. Als zweites können wir durch `git init` diesen Ordner als Repository initialisieren.

## Aufgabe
+ Lege einen Ordner `Facharbeit` an.
+ Führe `ls -a` aus.
+ Initialisiere jetzt das Git-Repository.
+ Führe noch einmal `ls -a` aus. Was fällt auf? Untersuche!

