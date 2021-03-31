# Minesweeper

Es gibt zwei Fälle in denen das Modul OS verwendet wird, in beiden Fällen funktionieren diese Befehle nur unter Windows.
Einmal beim Öffnen der Anleitung und das zweite Mal beim Öffnen des Links zum Repo.

Ich habe das Spiel auf folgender Grundlage implementiert:

Aufgabenstellung:

Minesweeper ist ein relativ altes Computerspiel, welches traditionsgemäß mit dem Betriebssystem Microsoft Windows mitgeliefert wurde. Ziel des Spiels ist es auf einem Rasterfeld durch logisches Denken und zufälligem Raten herrauszufinden, unter welchen Feldern Minen versteckt sind. Man gewinnt in dem man am Stück alle Felder aufdeckt, unter denen sich keine Minen befinden. Deckt man eine Mine auf, so verliert man das
Spiel. Deckt man ein Feld ohne Minen auf, so erscheint auf diesem Feld eine Zahl, welche einem anzeigt wieviele Felder mit Minen direkt an das eben aufgedeckte Feld angrenzen. Zusätzlich läuft zu jeder Partie eine Stoppuhr, so dass die Zeit gemessen wird die der
Spieler benötigt um das Spiel zu beenden. Implementiert mit Python eine lauffähige GUI-Version des Spiels Minesweeper. Im einzelnen soll das Programm folgendes leisten können:

• Zunächst hat man die Auswahl aus verschiedenen Schwierigkeitsstufen nach denen das Spielfeld aufgebaut und die Minen zufällig darunter platziert werden:
  – Leicht: Spielfeld 8x8 Felder und 10 Minen
  – Mittel: Spielfeld 16x16 Felder und 40 Minen
  – Schwer: Spielfeld 30x16 Felder und 99 Minen
  – Benutzerdefiniert: maximal 30x30 Felder und maximal 800 Minen
  
• Wird mit der linken Maustaste auf ein verdecktes Feld geklickt, so wird dieses aufgedeckt und der darunter liegende Inhalt wird angezeigt. Befand sich unter dem Feld eine Mine so wird dem Spieler angezeigt das er verloren hat, das gesamte Feld wird aufgedeckt und das Spiel ist beendet. Andernfalls wird an der Stelle des aufgedeckten Feldes eine Zahl (0 – 8) angezeigt, entsprechend der Anzahl an angrenzenden Minenfeldern. Wurden alle Felder, mit Außnahme der Minenfelder, aufgedeckt so ist die Partie gewonnen.

• Mit einem Rechtsklick wird ein verdecktes Feld als Minenfeld markiert. Mit einem weiterem Rechtsklick wird aus der Minenmarkierung eine Fragezeichenmarkierung, um anzuzeigen das man sich noch nicht ganz sicher ist ob unter dem Feld eine Mine liegt oder nicht. Ein weiterer Rechtsklick auf ein solches Feld entfernt jegliche Markierung wieder.

• So bald eine Partie gestartet wird, beginnt auch eine sichtbare Stoppuhr die Zeit bis zum Ende des Spiels zu messen. Wird ein Spiel gewonnen, so wird die Zeit in einer Toprangliste gespeichert, jedoch immer nur die 5 Bestzeiten für jeden der vier Schwierigkeitsmodi. Dem Spieler soll es möglich sein diese Ranglisten einzusehen.

• Neben der Stoppuhr soll dem Spieler auch ein einfacher Zähler angezeigt werden, welcher die als Minen markierten Felder mitzählt. Zudem soll es dem Spieler jederzeit möglich sein, das Spiel neuzustarten, d. h. alle Felder werden wieder verdeckt, jede Markierung entfernt, die Stoppuhr zurückgesetzt und die Minen werden erneut zufällig platziert.

• Zusätzlich soll sich der Spieler vom Computer einen Zug vorschlagen lassen können, dieser sollte nach Möglichkeit nicht zufällig raten und dem Spieler helfen die Partie zu gewinnen. Dabei soll diese einfache KI kein Wissen darüber haben, an welcher Stelle sich die Minen befinden.

Implementiert auch folgende Features:
• Im Originalspiel befindet sich unter dem ersten aufgedecktem Feld nie eine Mine.
• Befindet sich unter einem aufgedecktem Feld keine Mine und grenzen an diesem Feld auch keine Minen direkt an, so werden alle Felder um dieses aufgedeckt anstatt ein 0-Feld anzuzeigen. Befindet sich ein weiteres 0-Feld unter den automatisch aufgedeckten Feldern, so wird dieser Prozess rekursiv fortgeführt.
