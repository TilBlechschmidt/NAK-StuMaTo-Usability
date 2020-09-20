# Heuristische Analyse

## Methodik

Diese Arbeit verwendet eine heuristische Analyse als Expertenreview-Verfahren um formale Abweichungen von Erfahrungswerten der Usability festzustellen.

Dies wirkt einerseits ergänzend zu den späteren Nutzerverfahren, welche tatsächliche Probleme unvoreingenommener Nutzer hervorheben sollen und andererseits dient es dazu, potentielle Problemfelder zu identifizieren, welche der Direktion ebenjener Nutzerverfahren dienen können.

Dabei wird im Erfahrungsrahmen der Experten Bezug auf die Artefakte und Erkenntnisse der Kontextanalyse genommen, um aus dem Kontext der Anwendung ein erstes Verständnis für Eigenarten, aber auch besondere Anforderungen von StuMaTo zu erlangen.



### Ziele

Der Zweck der heuristischen Analyse ist eine Vertiefung des Verständnisses für problematische Zustände in der Anwendung.

Daraus ergeben sich hier zwei hauptsächliche Ziele:

1. Die Identifikation von eindeutig nutzerunfreundlichen Elementen zur Verwendung in der Gestaltungsphase. Diese sollten klar nutzerfeindlich und von lokalisierter Natur sein, sodass daraus entspringende Gestaltungsvorschläge unbestreitbar sinnvoll sind und keine übergreifenden Prozesse verändern.
2. Die Identifikation von Problemfeldern, welche einer genaueren Untersuchung bedürfen und somit eine Richtlinie für die Direktion von Nutzertests oder weiteren Analysen darstellen. Diese können, durch eine Rücksprache mit Stakeholdern und durch weitere Untersuchung entweder zu Problemelementen nach Punkt 1 überführt werden, oder zu überregionalen Änderungen am Design des Systems führen.

Mögliche Zielartefakte sind demnach Auflistungen dieser.



### Art der Untersuchung

Die vorliegende Untersuchung konzentriert sich auf eine heuristische Analyse unter Zuhilfenahme der Heuristiken nach Nielsen und Shneiderman. 

Dies deckt sich vor allem mit dem Ziel, formale Kriterien durch Expertenwissen nachzuprüfen.
Es ist hierdurch möglich, mit gering gehaltenem Zeitaufwand eine Basis für folgende Untersuchungen durch Nutzerverfahren zu schaffen, sodass diese Nutzerverfahren nicht ausschließlich auf der Grundlage der Kontextanalyse geplant werden. Die enge Verbindung mit den Nutzerverfahren erlaubt es, mithilfe dieser zusätzlich Fehleinschätzungen während der heuristischen Analyse aufzudecken.

Das Verfahren der heuristischen Evaluation erlaubt des Weiteren eine Abdeckung von formalen Kriterien mit begrenztem Expertenwissen und das sowohl in der Form einer summativen, als auch einer formativen Analyse.



Alternative Expertenverfahren wären zum Beispiel das Walkthrough-Verfahren und das DaTech-Prüfverfahren. Diese wurden jedoch unter Bevorzugung der heuristischen Evaluation nicht gewählt. 



**Gegen die Verwendung des Walkthrough-Verfahren sprachen die folgenden Punkte:**

- Zwei der Autoren hatten bereits eine starke Vertrautheit mit dem System, welches eine große Stärke dieses Verfahrens, die Ermittlung der explorativen Erlernbarkeit, unterminiert hätten.

  

- Die Verwendung dieses Verfahrens mithilfe von Nutzern wurde nicht in Erwägung gezogen, da dies einen deutlichen logistischen Aufwand für einen geringen Mehrwert darstellt, da fokussierte Nutzertests in einem Usability-Labor bereits vorgesehen waren.



- Dieses Verfahren einen geringen Fokus auf formale Usability-Prinzipien legt. Diese Prinzipien können jedoch für bestimmte Problemklassen eine präzisere Begründung für Usability-Probleme liefern, als eine subjektive Nutzer-Einschätzung. Die Berücksichtigung der Einschätzungen von Nutzern ist jedoch bereits durch die Nutzertests geplant und eine ausgeglichene Einschätzung von mehreren Seiten ist uns wichtig.



**Gegen die Verwendung des DaTech-Prüfverfahrens sprachen die folgenden Punkte:**

- Unter der Nutzung des DaTech-Prüfverfahrens ist die Unterscheidung zwischen einer schadhaften Abweichung und einer vorteilhaften alternativen Gestaltung sehr wichtig. Diese erfordert jedoch eine Erfahrung der durchführenden Experten, die wir nicht für uns beanspruchen können.



- Eine Zertifizierung der Anwendung ist weder Ziel noch besonders hilfreich.



- Grundlegende Prinzipien des Handbuchs sind ebenfalls in den Heuristiken der heuristischen Evaluation vorhanden.



- Zum Verständnis des komplexen Prüfhandbuches wäre eine deutlich längere Einarbeitung notwendig, welche nicht in einer sinnvollen Relation zum Nutzen des Einsatzes in dieser Arbeit stünde, zumal der Nutzen, den dieses Verfahren gesondert und im Vergleich zu anderen Verfahren zusätzlich bringt, unklar ist.



Aus demselben Grund, welcher auch gegen die Verwendung eines nutzerunterstützten Walkthroughs vorgebracht wurde, wurde sich gegen die Anwendung einer kooperativen heuristischen Evaluation entschieden. 

Stattdessen soll eine heuristische Evaluation aller drei Autoren, unabhängig voneinander, die großen Probleme der klassischen heuristischen Evaluation — ihre geringe Reliabilität und Objektivität – einschränken und durch den anschließenden Vergleich aus den Problemlisten eine gemeinsame, gewichtete Problemliste synthetisieren.



### Ablaufplan 

Diese parallele heuristische Analyse befolgt diesen Ablauf:

1. Kriteriensynthese (in @sec:heuristic:method:criteria genauer beschrieben)
2. Unabhängige Prüfung inkl. Notieren der Probleme
3. Erstellung einer gemeinsamen Gesamtliste
4. Unabhängige Gewichtung der Probleme der Gesamtliste
5. Gewichtung und Probleme diskutieren und zusammenfassen
6. Klare und lokalisierte Probleme erfassen und gewichten
7. Aus breiteren Trends innerhalb der Probleme Problemfelder erfassen
8. Daraus problematische Prozesse und Zustände zum weiteren Test durch Nutzer identifizieren
9. Im Nachgang zu den Nutzertests Nutzerergebnisse mit Expertenbewertung vergleichen



Die Vorbedingung dieses Ablaufes ist die vorangegangene Kontextanalyse.

Punkt 1 bis 5 des dargestellten Ablaufes formen eine klassische heuristische Analyse dar, welche besonders darauf gerichtet ist, Beeinflussungen zwischen den Evaluatoren zu vermeiden, indem stets erst am letzten möglichen Zeitpunkt ein Vergleich der Ergebnisse stattfindet. So werden zur Vereinheitlichung der Analyse und zur Sicherstellung auswertbarer Ergebnisse zwar dieselben Kriterien verwendet, die Bewertung der Anwendung anhand dieser erfolgt jedoch parallel. Nach der Zusammenführung der gefundenen Probleme erfolgt auch die Gewichtung dieser wieder parallel.

Punkt 6 bist 8 sind an das Format der Zielstellung gerichtet. Diese ermöglichen eine sinnvolle Verarbeitung innerhalb des vorgestellen Analyserahmens.

Punkt 9 dient der Rückkopplung an die Bewertung und kann dazu dienen, die in Punkt 8 erstellten Problemfelder zu bewerten und Fehler in der Bestimmung von Problemen in Punkt 6 zu erkennen. Letzteres ist besonders wichtig, um in der späteren Gestaltungsphase nicht fehlgeleitete, sich negativ auswirkende Änderungen vorzunehmen. Ersteres hingegen ist die Grundlage für größere Veränderungen in der Gestaltungsphase.



### Bestimmung der Analysekriterien {#sec:heuristic:method:criteria}

Die Heuristiken, welche zur Bewertung in dieser Phase der Analyse verwendet werden, werden durch eine Verbindung der Kriterien nach Nielsen und der Kriterien nach Shneiderman festgelegt. Diese sind publiziert und anerkannt und haben dadurch eine kanonische Beschreibung. Die Verbindung beider Kriterienmengen dient dabei der Vergrößerung des Bewertungsspektrums und der Verringerung der Abhängigkeit zu einer Person, die diese publiziert hat. 

Diese Kriterien werden zunächst von uns definiert, sehr ähnliche miteinander verbunden und redundante Kriterien werden eliminiert. Anschließend erfolgt eine Darstellung aller Kriterien in ihrem finalen Zustand.

Die Synthese der Kriterien erfolgt gemeinschaftlich, um allen eine Mitsprache zu erteilen und dennoch einen einheitlichen Konsens zu erreichen. Eine noch größere Unabhängigkeit der Evaluationen durch die Erstellung eigener Kriterien je Evaluator wurde vermieden, da diese die subjektiven Ansichten des Evaluators nicht nur in die Bewertung des Ist- sondern auch die Festlegung des Sollzustandes einbezogen hätte. Dies könnte entgegen zu den Zielen des parallelen Konzeptes eine Erhöhung der Subjektivität zur Folge haben und könnte ebenfalls durch Meinungsverschiedenheiten zwischen den Evaluatoren zu einem späteren Zeitpunkt die Auswertung erschweren.

 Die im Folgenden verwendeten Kriterien aus [@heur:shneiderman] und [@heur:nielsen] sind im Anhang respektive unter @sec:heuristiken-shneiderman und @sec:heuristiken-nielsen beschrieben.

Alle hier verwendeten Kriterien werden jedoch zugunsten des Leseflusses ins Deutsche übersetzt und teilweise dabei leicht verändert. Des Weiteren erhalten Sie eine originale Beschreibung nach dem Verständnis der heuristischen Evaluatoren, welches durch die Konsultation der eben genannten Beschreibungen gebildet wurde. Diese erneute Beschreibung und Bezeichnung sollen Missverständnisse zwischen Lesern und Evaluatoren vermeiden. Sollte bei der Verwendung der existierenden Kriterien ein abweichendes Verständnis der Kriterien bei Leser und Evaluator herrschen, würde dies die Aussagekraft der Analyse für den Leser mindern. 

In der Interpretation der Probleme wird jedoch ausschließlich die hiesige Definition zu Rate gezogen. Geschieht hierbei eine Verwechslung oder ein Missverständnis von Kriterien nach Nielsen und Shneiderman, ist der Vergleich zu diesen zwar schwierig, die Schlussfolgerung der Entscheidungen dieser Analyse leidet aber nicht.



### Analysekriterien

Von den Kriterien nach Nielsen werden folgende Kriterien übernommen:

- "Aesthetic and Minimalist Design" als "Relevanz der Kommunikation", da dieses Kriterium sich besonders auf die Vermeidung überflüssiger Informationen und weniger auf die eher subjektive Beschreibung der Ästhetik bezieht
- "Help users recognize, diagnose, and recover from errors" als "Konstruktive Fehlerbehandlung", da der Fokus darauf liegt, dem Nutzer konkret bei der Behandlung eines Fehlers zu unterstützen
- "Help and Documentation" nach [@heur:brau/sarodnick] als "Hilfe und Dokumentation" 

- "Match between system and the real world" als "Realitätsnahe Semantik und Vokabular", da die Bedeutung des Kriteriums sich besonders auf realitätsnahe Metaphorik konzentriert und weniger auf den Zustand der Welt und des Systems.

Von den Kriterien nach Shneiderman werden folgende Kriterien übernommen:

- "Design dialogs to yield closure" als "Abgeschlossene Aktionen"
- "Keep users in control" nach [@heur:dahm] als "Benutzerbestimmte Eingaben"


Darüber hinaus wird eine Reihe von Kriterien von Shneiderman und Nielsen aufgrund auftretender Redundanz oder thematischer Ähnlichkeit kombiniert:

- "Visibility of system status" und "Offer informative feedback." berühren ähnliche Themenkomplexe. Ersteres Kriterium beinhaltet dabei über das letztere hinaus auch die Sichtbarkeit länger anhaltenden Zustandes, während letzteres sich vor allem auf Zustände als Reaktion auf Aktionen bezieht. Diese beiden wurden darum als "Sichtbarer Systemstatus und Statusmeldungen" zusammengefasst.
-  "User control and freedom " und "Permit easy reversal of actions" als "Reversibiltät und Abbruchmöglichkeiten", da ersteres Kriterium das letztere in seiner Beschreibung enthält, aber besonders auch die Möglichkeit des Abbruchs zu jeder Zeit hervorhebt.
- "Consistency and standards" und "Strive for consistency." als "Konsistenz und Standardtreue", da sie sich sehr ähneln. Im Detail fokussiert sich ersteres eher auf die Konsistenz zu anderen Anwendungen und letzteres auf die interne Konsistenz, für den Nutzer stellt dies jedoch ein nahezu identisches Problem dar.

- "Error prevention" und "Prevent errors." sind als identische Kriterien in "Fehlerprävention" zusammengefasst.

- "Recognition rather than recall" und "Reduce short-term memory load." sind ebenfalls in ihrer Intention identisch und wurden nach [@heur:brau/sarodnick] als "Erkennen vor Erinnern" kombiniert
- "Flexibility and efficiency of use" und "Seek universal usability.", da ersteres in letzterem Kriterium enthalten ist. Dies ist als "Universelle Benutzbarkeit und Anpassbarkeit" bezeichnet.

Das Ergebnis dieses Verfahrens ist in +@tbl:mergecriteria und +@tbl:criteria aufgeführt.

| Nielsen                                                 | Extrahiertes Kriterium                      | Shneiderman                      |
| ------------------------------------------------------- | ------------------------------------------- | -------------------------------- |
| Match between system and the real world                 | Realitätsnahe Semantik und Vokabular        |                                  |
| Aesthetic and minimalist design                         | Relevanz der Kommunikation                  |                                  |
| Help users recognize, diagnose, and recover from errors | Konstruktive Fehlerbehandlung               |                                  |
| Help and documentation                                  | Hilfe und Dokumentation                     |                                  |
|                                                         |                                             |                                  |
|                                                         | Abgeschlossene Aktionen                     | Design dialogs to yield closure. |
|                                                         | Benutzerbestimmte Eingaben                  | Keep users in control.           |
|                                                         |                                             |                                  |
| User control and freedom                                | Reversibilität und Abbruchmöglichkeit       | Permit easy reversal of actions. |
| Visibility of system status                             | Sichtbarer Systemstatus und Statusmeldungen | Offer informative feedback.      |
| Consistency and standards                               | Konsistenz und Standardtreue                | Strive for consistency.          |
| Error prevention                                        | Fehlerprävention                            | Prevent errors.                  |
| Recognition rather than recall                          | Erkennen vor Erinnern                       | Reduce short-term memory load.   |
| Flexibility and efficiency of use                       | Universelle Benutzbarkeit und Anpassbarkeit | Seek universal usability.        |

Table: Herleitung der Kriterien der Heuristischen Evaluation {#tbl:mergecriteria}



Da in der Kontextanalyse beanstandet wurde, dass das System schlecht gepflegt und nicht aktuell ist, wird außerdem das Kriterium der "Aktualität und Pflege" gesondert betrachtet. Dies ist ein Problem, welches die Usability des Systems einschränkt, ohne jedoch zwingend eine klassische Heuristik zu sein. Der Fakt, dass Inhalte veraltet sind, ist in sich kein Designfehler, der behoben werden kann, kann sehr wohl jedoch ein Symptom zugrundeliegender Probleme sein. Darum wurde dieses Kriterium dennoch geschaffen, um diese Nutzeraussagen nachzuvollziehen und detaillierter zu verstehen. Hierzu wurden durch `Hendrik` und `Til` Analysen im Produktivsystem vorgenommen, da sie als Mitarbeiter von `ppi` auf dieses Zugriff haben.



Aus dem Verständnis dieser Kriterien entsprechend ihrer Beschreibung in [Anhang @sec:heuristik-beschreibungen] werden die folgenden Beschreibungen synthetisiert:

| Bezeichner | Kriterium | Beschreibung |
| --- | ----- | ------------ |
| ADAPT      | Universelle Benutzbarkeit & Anpassbarkeit   | Die Anwendung kann von Anwendern unterschiedlichster mit verschiedenen Eigenschaften, Fähigkeitsstufen und Erfahrungen verwendet werden. Sowohl Anfänger, als auch Experten werden vom System adäquat unterstützt, ohne die jeweils andere Gruppe zu beeinträchtigen. Die Anwendung ist dazu auf die Bedürfnisse von Nutzern anpassbar. |
| CLOSURE    | Abgeschlossene Aktionen                     | Aktionen sind in sich klar abgeschlossen und es ist offensichtlich, wenn ein Arbeitsabschnitt beendet ist – idealerweise bereits vor dem Abschluss.  Ein Nutzer bekommt Feedback bei Abschluss einer Operation.                                                                                                                         |
| CONSIST    | Konsistenz und Standardtreue                | Die Anwendung zeigt für ähnliche Situationen ein gleichartiges Verhalten und ist demnach wieder erkennbar. Sie hält sich an bekannte Standards in anderen Systemen, um auch im Bezug zu diesen Wiedererkennbarkeit zu ermöglichen und erlernbar zu sein.                                                                                |
| CONTROL    | Benutzerbestimmte Eingaben                  | Die Handlungen im System werden durch den Nutzer bestimmt, er beherrscht die Interaktion mit dem System. Das System weicht nicht von den grundlegenden Erwartungen an die Konsequenzen einer  Nutzerhandlung hab und zwingt den Nutzer auch nicht, Handlungen oder Eingaben unnötig zu wiederholen.                                     |
| ERR-HANDLE | Konstruktive Fehlerbehandlung               | Treten Fehler auf, ermöglicht das System dem User mithilfe verständlicher diagnostischer Hinweise zu reagieren. Diese Hinweise sind menschenlesbar und bieten wertvolle, konstruktive Hinweise auf potentielle Fehlerursachen und zu Behebungsmöglichkeiten.                                                                            |
| ERR-PREV   | Fehlerprävention                            | Der Nutzer wird vom System daran gehindert, destruktive Handlungen – vor allem unabsichtlich – auszuführen oder das System in Fehlzustände zu leiten. Das System ist des Weiteren klar und verständlich, um auch Verwechslungen und daraus folgende semantische Fehler zu vermeiden. Unsinnige Eingaben werden nicht zugelassen.        |
| HELP       | Hilfe und Dokumentation                     | Es existiert eine Möglichkeit auf Hilfestellungen und Verhaltensdokumentation des Systems zuzugreifen, falls es nötig ist.                                                                                                                                                                                                              |
| REAL       | Realitätsnahe Semantik und Vokabular        | Das System verwendet Begriffe und Metaphern aus der realen Welt, mit denen eine intuitive Verbindung hergestellt werden kann. So erscheint das System für den Nutzer durch seine Erfahrung mit der Welt logisch und sinnvoll.                                                                                                           |
| RECOG      | Erkennen vor Erinnern                       | Das Kurzzeitgedächtnis des Nutzers wird geschont, indem ein intuitives Verständnis ermöglicht wird und indem Daten nicht über mehrere Ansichten hinweg gemerkt werden müssen. Dringend notwendige Informationen können stets aus der aktuellen Ansicht erlangt werden.                                                                  |
| RELEV      | Relevanz der Kommunikation                  | Das System beschränkt sich auf die Kommunikation der notwendigen Informationen. Überschüssige Kommunikation, welche lediglich die Sichtbarkeit wichtiger Informationen verschlechtert, werden vermieden.                                                                                                                                |
| STATUS     | Sichtbarer Systemstatus und Statusmeldungen | Relevante interne Zustände des Systems werden dem Nutzer mitgeteilt, z.B. spezielle Modi in denen er sich befindet, Ladezeiten, Fehlerzustände, oder der Speicherzustand der aktuell betrachteten Daten. Besonders wichtig sind hier auch Statusmeldungen als Reaktion auf Aktionen des Nutzers.                                        |
| UNDO       | Reversibilität und Abbruchmöglichkeit       | Der Nutzer behält die Kontroller über den Kontrollfluss, er kann Aktionen abbrechen, sie rückgängig machen und rückgängig gemachte Aktionen wiederholen. So wird dem Nutzer die Angst vor den Konsequenzen ungewollter Aktionen genommen.                                                                                               |
| UPTODATE | Aktualität und Pflege | Das System ist gut gepflegt und verwendbar, es existieren notwendige Datengrundlagen für eine bedeutsame und hilfreiche Interaktion zwischen Nutzer und System. Das System unterstützt die Interaktion zur Sicherstellung eines gepflegten Systems. |

Table: Verwendete Kriterien der Heuristischen Evaluation {#tbl:criteria}



### Weitere Analyse-Parameter

Die Funde aus der Bewertung der Anwendung nach den beschriebenen Heuristiken werden mit ihrem Fundort dokumentiert und gewichtet. Eine Zuordnung zu mehreren Heuristiken ist möglich, in der nachfolgenden Auswertung wird ein Problem dann je einmal unter jeder zugeordneten Heuristik aufgeführt, da ein Verstoß gegen mehrere Heuristiken damit auch mehrfach gewürdigt werden sollte. Zur Dokumentation des Fundortes werden die katalogisierten Ansichten und Dialoge aus [Anhang @sec:appendix:screens] verwendet. Ist ein Problem als Problem der gesamten Anwendung und nicht eines Dialogs im Besonderen zu verstehen, so wird kein Fundort zugeordnet. 



Die Gewichtung von Problemen, dargestellt in +@tbl:weighting-definition, ist in 4 Stufen aufgeteilt. Zu beachten ist hierbei die Bewertungsstufe 0. Diese wurde aufgenommen, da in der vorgestellten Methodik Evaluatoren auch eine Bewertung der Schwere von Problemen, die sie nicht angemerkt haben, vornehmen. So kann eine Uneinigkeit ob der gefundenen Probleme auch in der Auswertung noch dargestellt und nachvollzogen werden. Die ebenfalls unorthodox erscheinende Bewertungsstufe 1 signalisiert die Notwendigkeit, die Gültigkeit eines Problems vermehrt durch Nutzertests abzusichern, besonders wenn vermutet wird, dass damit nur potentiell bestimmte Nutzergruppen betroffen sind. Dies bedeutet allerdings nicht, dass ernsthafte Probleme, die "nur" eine gut verstandene, aber vielleicht kleine Nutzergruppe betreffen, hiermit bewertet werden sollen. So wären fehlende "Accessibility"-Features, welche nur eine Gruppe körperlich eingeschränkter Menschen betreffen, keineswegs pauschal in die Gewichtung 1 einzuordnen und damit geringer zu bewerten als kosmetische Probleme. Vielmehr steht die Unklarheit, ob Anforderungen, die eine gegebene Situation zum Problem machen würden, überhaupt gegeben sind.



| Gewichtung | Bedeutung                                                    |
| ---------- | ------------------------------------------------------------ |
| 0          | Kein Usability-Problem                                       |
| 1          | Könnte je nach Nutzer potentiell ein geringes Problem darstellen |
| 2          | Kosmetisches Problem mit Einfluss auf das Nutzungserlebnis   |
| 3          | Problem mit Einfluss auf den Erfolg einer Interaktion        |

Table: {#tbl:weighting-definition}

## Ergebnisse

Die Auflistung der Problemfunde je Evaluator (), aber auch die Vereinigung dieser sind als Rohergebnisse aus Gründen der Übersichtlichkeit in [Anhang @sec:heuristik-rohergebnisse] nachverfolgbar.  Ebenfalls dort nachzuschlagen ist die Gewichtung dieser Probleme je Evaluator.

Hier erfolgt stattdessen eine Bearbeitung aggregierter Daten aus diesen Ergebnislisten.








### Endgültiges Ergebnis

Die Berechnung der Abweichung der Schwere eines Problems ist wie folgt und drückt damit die Summe der Differenzen zwischen den einzelnen Bewertungen aus.



$$Sei~g(x),~x\geq1~die~Schwere~nach~Evaluator~Nr.~x.  $$

$$Sei~n~die~Anzahl~der~Evaluatoren.$$

$$Abweichung = \sum_{i=1}^{n}{\sum_{j=i+1}^{n}{|g(i)-g(j)|}}$$



Eine höhere Abweichung ist demnach mit einer höheren "Kontroverse" zwischen den Bewertern ob der Schwere des Problems zu verstehen. Eine geringere Abweichung hingegen spricht für einen Konsens.

| Bezeichner | Kriterium | Fundort | Beschreibung | Schwere | Abweichung |
| ---------- | --------- | ------- | ------------ | ------- | ---------- |
|            |           |         |              |         |            |
|            |           |         |              |         |            |
|            |           |         |              |         |            |
Table: Finales Ergebnis der heuristischen Analyse {#tbl:heur:final}

![Gewichtungshäufigkeit je Kategorie](src/images/stacked-bar.pdf)

- Auswertungen:
  - höchst gewichtete
  - Visualisierung Gewichtung + Anzahl je Kriterium
  - höchste Varianz der Gewichtung
  - 


### Ergebnisse (Hendrik)

Diese Heuristische Analyse wird im Produktivsystem von StuMaTo durchgeführt. Dies hat den Vorteil, dass sie mit denselben Daten befüllt sind, mit denen auch die Interviewten der Kontextanalyse bisher gearbeitet haben.

Die meisten Fehler treten in StuMaTo in der Heuristik Übereinstimmung mit der Realen Welt auf. Zuerst fällt auf, dass im Startbereich keine Aufgaben verfügbar sind. Dies kann nicht mit der realen Welt übereinstimmen, da es Aufgaben geben muss, die von den Studenten bearbeitet werden können. Somit ist es auch nicht möglich sich auf eine Aufgabe zu bewerben.
In der Studentenübersicht fällt aus, dass ehemalige Studenten weiterhin als Studenten geführt werden und nicht in der Kategorie Alumni & Alumnae gelistet sind. Zudem ist bei Studenten, die in einem Jahrgang sind, nicht immer dasselbe Semester angegeben. Hier unterschieden diese sich um ein Semester. Bei einem Blick in die Studentenprofile fallen die nächsten Probleme auf. In der Verfügbarkeitsübersicht werden die ältesten Daten zuerst angezeigt. Dies kann verwirren, da die aktuellsten Daten am relevantesten sind. Um diese einsehen zu können, muss mit der Scrollbar zunächst nach rechts gescrollt werden. Zudem ist das aktuelle Datum in dieser Verfügbarkeitssicht nicht einsehbar. In der Verfügbarkeitsübersicht fällt zudem auf, dass diese bei nahezu allen Studenten große Lücken aufweist. Dies ist eine Abweichung zur realen Welt, da alle Studenten in ihren Praxisphasen Aufgaben bearbeitet haben, die sie hätten in StuMaTo aufnehmen können. Positiv anzumerken ist jedoch, dass Semester- und Urlaubszeiten überall tadellos gepflegt sind. Wenn eine Aufgabe in die Verfügbarkeitsübersicht eingefügt werden soll tritt das Problem auf, dass viele Aufgaben nicht im System hinterlegt sind. Dies ist besonders kritisch, da bei der Aufgabe auch kein Freitextfeld referenziert werden kann. Zudem kann über diesen Dialog auch keine neue Aufgabe angelegt werden.

In der Kategorie Sichtbarkeit des Systemstatus fallen kleinere Fehler auf. Bei den zugeordneten Studenten in einer Aufgabe, sieht es so aus als könne man auf sie klicken, jedoch passiert danach nichts. Dasselbe gilt für die Kenntnisse bei der Anlage einer neuen Aufgabe. Auch hier verändert sich der Cursor zur Hand, so dass der Nutzer erwarten würde, dass nach einem Klick eine Aktion ausgeführt wird. Dies ist jedoch nicht der Fall. Ein weiterer Verstoß gegen die Heuristik Sichtbarkeit des Systemstatus ist bei der Verwaltung der Studenten zu finden. Wenn die Rolle eines Mitarbeiters zu Student oder Betreuer geändert wird, bleibt in der GUI die Rolle des Studenten zunächst erhalten. Erst beim Neuladen der Seite wird die Rolle auch in der Oberfläche richtig angezeigt.


1. Keine Aufgaben sind im Startbereich zu sehen
2. Suchfeld wird vom Passwortmanager erkannt
3. Ehemalig Studenten werden als Studenten geführt
4. Verfügbarkeitsslider ist nicht auf das aktuelle Datum gezeigt
5. Profile sind wenig gepflegt
6. Standort von Aufgabe ist schlecht dokumentiert
7. Semesterangaben sind bei einigen Studenten um ein Semester versetzt
8. Es können nicht alle wissenschaftlichen Arbeiten auf einmal gefunden werden
9. Studenten in den Aufgaben sehen aus, als könnte man sie anklicken, aber nicht passiert danach
10. Aufgabenstatus sind auf Englisch, wenn der Rest der Anwendung auf Deutsch ist 
11. Meine Aufgabe kann ich bei neuer Kalendareintrag nicht finden.
12. Ich kann da auch keine neue Aufgabe anlegen
13. Kenntnisse sehen aus als wären sie clickbar beim Anlegen einer Aufgabe
14. Ich weiß nicht, was für eine Mail versendet wird, wenn ich auf Interesse drücke
15. Kontraste im Darkmode sind nicht gut, Elemente könnten übersehen werden
16. Bei Skills ist nicht klar, bei welchem Skill ich mich selber einordnen soll
17. Kein https, Unsicherheit
18. Wenn Zustand von Mitarbeiter geändert, wird dies nicht in der UI angezeigt
19. Aufteilung Aufgaben/daueraufgaben





## Reflexion der Methodik

- Hätte etwas detailliertere durchgeführt werden können
- mit der Methodik relativ zufrieden
- errungene Ergebnisse:
  - konnten Interviewvermutungen bestätigen?
  - konnten für Nutzertests Schwerpunkte finden?
- Zunächst Missverständnisse in der Bedeutung der Heuristiken
  - große Schwäche
- statistische Auswertung ist nur begrenzt aussagefähig, auch mit Gewichtung
- eine klarere Definition / Methode, wie man "eindeutig nutzerunfreundliche Elemente" von zu untersuchenden Problemfeldern trennt wäre hilfreich 