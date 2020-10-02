\newpage
# Heuristische Analyse {#sec:heur-anal}

## Methodik

Diese Arbeit verwendet eine heuristische Analyse als Expertenreview-Verfahren um formale Abweichungen von Erfahrungswerten der Usability festzustellen.

Dies wirkt einerseits ergänzend zu den späteren Nutzerverfahren, welche tatsächliche Probleme unvoreingenommener Nutzer hervorheben sollen und andererseits dient es dazu, potentielle Problemfelder zu identifizieren, welche der Direktion ebenjener Nutzerverfahren dienen können.

Dabei wird im Erfahrungsrahmen der Experten Bezug auf die Artefakte und Erkenntnisse der Kontextanalyse genommen, um aus dem Kontext der Anwendung ein erstes Verständnis für Eigenarten, aber auch besondere Anforderungen von StuMaTo zu erlangen.

<!-- TODO muss das hier wirklich sein? mehr auf die Szenarien münzen! -->
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



### Ablaufplan {#sec:heuristic:plan}

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
| :---------------------------------------------------- | :----------------------------------------------------: | ----------------------------------------------------: |
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

<!-- TODO change names? -->

Aus dem Verständnis dieser Kriterien entsprechend ihrer Beschreibung in [Anhang @sec:heuristik-beschreibungen] werden die folgenden Beschreibungen synthetisiert:

| Bezeichner | Kriterium                                   | Beschreibung                                                                                                                                                                                                                                                                                                                            |
| :--------------- | --------------------------------------------: | -------------------------------------------------------------------------------------------------------- |
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
| UPTODATE   | Aktualität und Pflege                       | Das System ist gut gepflegt und verwendbar, es existieren notwendige Datengrundlagen für eine bedeutsame und hilfreiche Interaktion zwischen Nutzer und System. Das System unterstützt die Interaktion zur Sicherstellung eines gepflegten Systems.                                                                                     |

Table: Verwendete Kriterien der Heuristischen Evaluation {#tbl:criteria}



### Weitere Analyse-Parameter

Die Funde aus der Bewertung der Anwendung nach den beschriebenen Heuristiken werden mit ihrem Fundort dokumentiert und gewichtet. Eine Zuordnung zu mehreren Heuristiken ist möglich, in der nachfolgenden Auswertung wird ein Problem für Auswertungen bezüglich der Kriterien dann je einmal unter jeder zugeordneten Heuristik aufgeführt, da ein Verstoß gegen mehrere Heuristiken damit auch mehrfach gewürdigt werden sollte. In Auswertungen, die sich nicht spezifisch auf bestimmte Kriterien beziehen, wird ein Problem jedoch nicht mehrfach gezählt, um die Gesamtanzahl nicht zu verfälschen. Zur Dokumentation des Fundortes werden die katalogisierten Ansichten und Dialoge aus [Anhang @sec:appendix:screens] verwendet. Ist ein Problem als Problem der gesamten Anwendung und nicht eines Dialogs im Besonderen zu verstehen, so wird kein Fundort zugeordnet.

Die Gewichtung von Problemen, dargestellt in +@tbl:weighting-definition, ist in 4 Stufen aufgeteilt. Zu beachten ist hierbei die Bewertungsstufe 0. Diese wurde aufgenommen, da in der vorgestellten Methodik Evaluatoren auch eine Bewertung der Schwere von Problemen, die sie nicht angemerkt haben, vornehmen. So kann eine Uneinigkeit ob der gefundenen Probleme auch in der Auswertung noch dargestellt und nachvollzogen werden. Die ebenfalls unorthodox erscheinende Bewertungsstufe 1 signalisiert die Notwendigkeit, die Gültigkeit eines Problems vermehrt durch Nutzertests abzusichern, besonders wenn vermutet wird, dass damit nur potentiell bestimmte Nutzergruppen betroffen sind. Dies bedeutet allerdings nicht, dass ernsthafte Probleme, die "nur" eine gut verstandene, aber vielleicht kleine Nutzergruppe betreffen, hiermit bewertet werden sollen. So wären fehlende "Accessibility"-Features, welche nur eine Gruppe körperlich eingeschränkter Menschen betreffen, keineswegs pauschal in die Gewichtung 1 einzuordnen und damit geringer zu bewerten als kosmetische Probleme. Vielmehr steht die Unklarheit, ob Anforderungen, die eine gegebene Situation zum Problem machen würden, überhaupt gegeben sind.

| Gewichtung | Bedeutung                                                        |
| ---------- | ---------------------------------------------------------------- |
| 0          | Kein Usability-Problem                                           |
| 1          | Könnte je nach Nutzer potentiell ein geringes Problem darstellen |
| 2          | Kosmetisches Problem mit Einfluss auf das Nutzungserlebnis       |
| 3          | Problem mit Einfluss auf den Erfolg einer Interaktion            |

Table: Definition der genutzten Gewichtungskategorien {#tbl:weighting-definition}

Da mehrere Evaluatoren im Ablauf der erklärten Methodik eine Gewichtung abgeben, bevor diese in einer Gewichtung zusammengefasst werden, wird mit der folgenden Metrik zusätzlich ein Sinn für die Eindeutigkeit der Gewichtung unter den Evaluatoren geschaffen:

Die Berechnung der Abweichung der Schwere eines Problems ist wie folgt und drückt damit die Summe der Differenzen zwischen den einzelnen Bewertungen aus.

$$Sei~g(x),~x\geq1~die~Schwere~nach~Evaluator~Nr.~x. Sei~n~die~Anzahl~der~Evaluatoren.$$
$$Abweichung~\Delta= \sum_{i=1}^{n}{\sum_{j=i+1}^{n}{|g(i)-g(j)|}}$$

Eine höhere Abweichung ist demnach mit einer höheren "Kontroverse" zwischen den Bewertern ob der Schwere des Problems zu verstehen. Eine geringere Abweichung hingegen spricht für einen Konsens.

\clearpage

## Ergebnisse

Der Ablauf nach [Abschnitt @sec:heuristic:plan] ist im [Anhang @sec:heuristik-rohergebnisse] gewissentlich dokumentiert. Die gemeinsame Problemliste ohne Gewichtung, welche zur Durchführung der Gewichtung verwendet wurde, ist nicht aufgeführt, da diese redundant zur finalen Ergebnisliste in +@tbl:heur:final ist. Stattdessen werden die einzelnen Gewichtungen anhand der Problembezeichner in der +@tbl:heur:weighted aufgeführt.

 Aus Gründen der Übersichtlichkeit wird an dieser Stelle jedoch nicht mit diesen Rohdaten gearbeitet, sondern lediglich mit aggregierten oder besonders interessanten Teildaten. In der Betrachtung der folgenden Daten ist zusätzlich zu beachten, dass einige der angemerkten Usability-Probleme vermutlich auch als reine Implementierungsfehler gesehen werden können. Sie wurden hier aber in keinster Weise ausgeschlossen. Das liegt darin begründet, dass eine Unterscheidung von schlechtem Design und schlechter Implementierung mangels Aussagekräftiger Systemspezifikation schwierig und potentiell willkürlich wäre, worunter die Qualität der Ergebnisse und der Methodik sinken würde. Darüber hinaus schränken diese Probleme, ob Implementationsfehler oder Designfehler, eine Einschränkung der User Experience dar und sollten erwähnt werden. Die folgenden Kapitel der Arbeit sind jedoch nicht auf die Betrachtung solcher Probleme, die als in dieser Weise uneindeutig erschienen, ausgerichtet. Dies ist möglich, da eine Betrachtung all der gefunden Usability-Probleme im Detail den Rahmen dieser Arbeit ohnehin übersteigen würde.



### Quantitative Gesamtkennzahlen

Mit der bloßen Anzahl $N$ der Problemfunde und deren Gewichtungen $G$, sowie der Abweichungen $\Delta$ kann ein grober Überblick über die Datenmenge verschafft werden:

Bei der Betrachtung der Rohmenge der Problemfunde ist $N=72$, wobei sowohl der Durchschnitt, als auch der Median von $G$ über alle Evaluatoren 2 ist. Dies ist nicht weiter verwunderlich, da aufgrund der festgelegten, diskreten Werte keine besonderen "Ausreißer" einen signifikanten Unterschied zwischen diesen erklären könnten. Diese Werte sind unter alle Evaluatoren des Weiteren sehr ähnlich, alle erreichten denselben Median und sehr ähnliche Durchschnitte (zwischen 1,93 | 1,96 | 2,11). Das arithmetische Mittel über die finalen Gewichtungen erreich einen leichten Anstieg auf 2,05. Der hier wirkende Effekt ist vermutlich, dass erst bei der Diskussion der Schwere der Probleme untereinander ein vollständiges Verständnis für diese eingetreten ist, wo sie vorher noch unterschätzt wurden.  

Zur Betrachtung der der Daten nach Kategorien wurde als zweite Datengrundlage jeder Datensatz, dem mehrere Kategorien zugeordnet waren, dupliziert, um diese mehrfachen Datensatz in der Untersuchung der Kategorien verwenden zu können. Für eine Betrachtung von einzigartigen Kategorienmengen waren diese Mehrfachzuordnungen zu selten. In der einzigartigen Kombination einer zugeordneten Kategorie und eines Problems ergibt sich $N'=80$.

In @fig:rel-weights ist die relative Häufigkeit der einzelnen Gewichtungskategorien ersichtlich.


![Relative Gewichtungshäufigkeit](src/images/pie.pdf){#fig:rel-weights}

Die Kategorie $0$ wurde in der finalen Ergebnisliste effektiv eliminiert, da diese aussagt, dass hier kein Problem vorliegt. Diese wurde zwar in den einzelnen Gewichtungen der Evaluatoren insgesamt 8 mal gewählt, jedoch kam es stets zu einer Einigung, welche die finale Gewichtung auf einen anderen Wert festgelegt hatte. Dabei wurde häufig die finale Gewichtung $1$ gewählt, da die Uneinigkeit darüber, ob ein Zustand überhaupt ein Problem ist, dafür spricht, dass dieses entsprechend der Definition der Gewichtung $1$ nutzergruppenabhängig sein könnte.

Die anderen Kategorien sind weitesgehend ausgeglichen, auch wenn die Gewichtung $2$ am häufigsten auftritt. Dennoch spricht der Anteil von 30%, welcher auf die Gewichtung $3$ entfällt dafür, dass die Anwendung einige ernste Usability-Probleme hat.



### Quantitativer Vergleich der Problemkategorien

Ein quantitativer Vergleich der einzelnen Problemkategorien ist in @fig:weight-per-category und @fig:delta-per-category vorgenommen. Hier können zum einen die Häufigkeit, mit der Gewichtungen im finalen Ergebnis aufgetaucht sind, pro Kategorie nachverfolgt werden und gleichzeitig der Konsens zwischen den Evaluatoren bezüglich einer Kategorie betrachtet werden. 

In der Häufigkeit der Problemgewichtungen sticht die Kategorie CONTROL mit einem besonders hohen Anteil von schweren Problemen heraus. Eben diese wird jedoch auch mit einem vergleichsweise hohen durchschnittlichen Abweichungswert heraus. Scheinbar scheinen hier also potentiell schwere Probleme aufzutreten, die jedoch nicht besonders klar verstanden sind. Das Kriterium CONSIST ist ebenfalls ein sehr umstrittenes Kriterium, welches zudem die größte absolute Problemhäufigkeit aufweist, wobei diese Probleme jedoch überwiegend kosmetischer Art oder sogar nutzergruppenabhängig sind. Noch umstrittener, wenn auch leicht weniger häufig sind die Probleme der Kategorie RELEV.

Im Gegensatz hierzu fällt das Kriterium ERR-PREV auf: Trotz dessen, dass es eine hohe Zahl an Problemen aufweist, besteht hier eine weitaus geringere Abweichung zwischen den Evaluatoren.  Es erscheint dadurch klar, dass die Anwendung einiges Verbesserungspotential in der Fehlerprävention aufzuweisen hat. Die quantitativ unscheinbar wirkenden Kategorien CLOSURE, ERR-HANDLE und UNDO sind in völliger Einstimmigkeit bewertet worden. Hier treten des Weiteren vermehrt Probleme der Gewichtung $3$ auf. 

\newpage

\begin{figure}[t]
\includegraphics{src/images/stacked-bar.pdf}
\caption{Gewichtungshäufigkeit je Kategorie}
\label{fig:weight-per-category}
\end{figure}
\begin{figure}[b ]
\includegraphics{src/images/bar-dev.pdf}
\caption{Durchschnittsabweichung je Kategorie}
\label{fig:delta-per-category}
\end{figure}

\clearpage

Da besonders ERR-HANDLE und UNDO besonders eng mit ERR-PREV verwandt sind, scheint generell ein größeres Problempotential in der Peripherie von Fehlern zu bestehen.  Der Umstand, dass die Kategorie UNDO lediglich ein Problem aufweist, wird hier von der Beschreibung dieses Problems, welches sich auf die gesamte Anwendung bezieht, überwogen: "Keine Möglichkeit, Änderungen rückgängig zu machen oder auch nur nachzuverfolgen". 
Das durch die Kontextanalyse mit aufgenommene Kriterium UPTODATE hat durchaus eine überdurchschnittliche Menge an Problemen, meist kosmetischer Natur, mit großer Varianz  hervorgerufen. Es sollte demnach in den Nutzertests weiterverfolgt werden, um mögliche Gründe für die schlechte Pflege des Systems herauszuarbeiten.

Entsprechend dieser Analyse der Aggregatsdaten erscheint es sinnvoll, besonders den Umgang mit Fehlern in der Anwendung in den folgenden Nutzertests zu untersuchen.  Eine Möglichkeit zur Nachverfolgung und zur Wiederherstellung von Systemzuständen sollte in der Designphase zumindest in Erwägung gezogen werden, besonders wenn Gebiete mit besonders hohen Fehlerquoten identifiziert werden können. Das Themengebiet Fehlerbehandlung kann damit ganzheitlich als Problemfeld entsprechend Ziel Nr. 2 der Heuristischen Evaluation betrachtet werden. Besonders kritisch sollte auch das Kriterium CONTROL betrachtet werden. Dieses ist in seiner Definition und in der Sicherheit der Probleme weniger klar, was eine Nachverfolgung und Verifikation in Nutzertests jedoch aufgrund der Signifikanz der potentiellen Probleme sehr interessant macht. Auch dieses Kriterium ist demnach so ein Problemfeld.

Diese Aggregation zeigt jedoch keine Kriterien, welche besonders für ein Extraktion von klaren, lokalisierten und kosmetischen Problemen nach Ziel Nr. 1 geeignet wären - zum Einen, da Problemkriterien ohnehin eine relativ breite Klassifikation wären, welche für konkrete, lokale Probleme eher weit gefasst wäre, und zum Anderen, da die Kriterien mit einer großen Menge von kosmetischen Problemen (Gewichtung $2$) auch eine hohe Abweichung zwischen den Evaluatoren aufweisen. Demnach ist es nicht ohne Weiteres möglich, diese als eindeutig nutzerunfreundlich herauszustellen.

### Betrachtung von einstimmig gewichteten Probleme

 Aufgrund der Beschränkungen dieser Arbeit, können nicht alle Probleme in gleicher Art analysiert und für die weitere Betrachtung verwendet werden. Sehr wohl können jedoch bestimmte Probleme genauer betrachtet werden. Im vorangehenden Abschnitt wurden bereits einige Kriterien genannt, welche eine besonders geringe Abweichung zwischen den Evaluatoren vorwiesen. Hier wird auf diese Aggregation nach Kriterien verzichtet und es werden als Auszug der Gesamtdaten stattdessen Probleme betrachtet, welche einstimmig mit der Gewichtung $3$ oder $2$ versehen wurden.

In +@tbl:critical-problems und +@tbl:cosmetical-problems sind deshalb jene Probleme, welche respektive eine einstimmige Gewichtung von $3$ oder $2$ erhalten haben, aufgelistet. 

|      Bezeichner      |        Kriterium        |                         Beschreibung                         |                         Fundorte                          |
| :------------------: | :---------------------: | :----------------------------------------------------------: | :-------------------------------------------------------: |
|ENDLESS-PROFILE|CLOSURE|Bei Bearbeitung des Studentenprofils ist der Abschluss von Aufgaben nicht klar, es kann ewig ohne klare Abfolge editiert werden.|STUDENT.UNI, STUDENT.WORK|
|CP-FEEDBACK|CLOSURE|Das Speichern von Credit Points gibt wenig Feedback bei der Bestätigung der Eingabe. Insgesamt ist es schwer ersichtlich, dass man die Eingabe noch manuell abschließen muss, der Prozess ist nicht atomar.|STUDENT.UNI|
|SKILLS-SAVED|CLOSURE, STATUS|Das Verändern der Kenntnisse ruft keine Speicheroperation hervor und durch eine Speicheroperation wird keine Rückmeldung hervorgerufen, die die Aktion für den Nutzer abschließt|STUDENT.WORK|
|TFL-EDIT|CONTROL|Eingetragene TFLs können nicht editiert, sondern nur neu angelegt werden.|STUDENT.UNI|
|TASK-FOR-CALENDAR|CONTROL, RECOG|Beim Anlegen eines neuen Kalendereintrags sind Aufgaben schwer auffindbar und können nicht neu angelegt werden. Der Nutzer muss sich den Namen der Aufgabe gemerkt haben.|STUDENT.WORK.NEW-ENTRY|
|NO-ERROR-TFL-UPLOAD|ERR-HANDLE|Bei einem provozierten Fehler wurde kontinuierlich gespeichert, ein Abbrechen war nicht möglich oder keine Fehlermeldung wurde angezeigt. (Hochladen von Dateien)|STUDENT.UNI.NEW-TFL|
|DIRTY-PROFILE-LEAVE|ERR-PREV|Bei editierten Credit Points oder Kenntnissen im Profil keine Nachfrage beim Verlassen der Seite|STUDENT.WORK|
|CANCEL-TASK-EDIT|ERR-PREV|Kein Nachfragen wenn geänderte Aufgabe nicht gespeichert und dann abgebrochen oder die Seite verlassen wird|TASK.EDIT|
|ADD-SKILL-WITH-DIRTY|ERR-PREV|Wenn man eine Kenntnis verändert, nicht speichert und dann eine neue Kenntnis hinzufügt dann werden die Änderungen an der ersten Kenntnis verworfen.|STUDENT.WORK|
|UNSEEN-DIRTY|RECOG, STATUS, ERR-PREV|Nicht abzusehen ob eine editierte Aufgabe,CP,Kenntnisse bereits gespeichert oder noch "dirty" ist.|STUDENT.*|
|UNDO|UNDO|Keine Möglichkeit, Änderungen rückgängig zu machen oder auch nur nachzuverfolgen|*|
|NO-TASKS|UPTODATE|Keine Aufgaben sind im Startbereich zu sehen|TASK.ALL|
|PROFILES|UPTODATE|Profile sind wenig gepflegt und nicht aktuell.|STUDENT.*|
Table: Kritische Probleme (einstimmig) {#tbl:critical-problems}



Bei diesen kritischen Problemen fällt besonders die Häufigkeit der Fundorte STUDENT.\*, also aller Unterseiten der Seite "Studenten", insbesondere die Tabs der Studentenprofile, auf. Diese scheinen von kritischen Problemen geplagt zu sein. Die Probleme könnten hierbei vermehrt auch Veränderungen am Prozess, in dem sie auftreten, erfordern, oder aber nicht nur lokal relevant sind. So erscheint es wahrscheinlich, dass die Möglichkeit, Änderungen nachzuverfolgen und Zustände wiederherzustellen (Problem UNDO) einen aufwändigeren Design-Prozess erfordern könnte. Auch die Probleme TASK-FOR-CALENDAR, CP-FEEDBACK oder ENDLESS-PROFILE könnten einen solchen Aufwand erfordern. Andere, wie UNSEEN-DIRTY, CANCEL-TASK-EDIT, DIRTY-PROFILE-LEAVE, ADD-SKILL-WITH-DIRTY erfordern mehr Arbeit der Kategorie Implementierung, als Design.

|      Bezeichner      |        Kriterium        |                         Beschreibung                         |                         Fundorte                          |
| :------------------: | :---------------------: | :----------------------------------------------------------: | :-------------------------------------------------------: |
|DARK|ADAPT, CONSIST|Schlechte Kontraste im Darkmode.|MANAGE, TASK.*, FAQ, STUDENT.WORK, Lade-Indikatoren,Tabs,|
|SEARCH-LAYOUT|CONSIST|Layout von Suchergebnissen ist nicht einheitlich.|SEARCH|
|NEW-SKILL-REENTRY|CONTROL|Suchergebnis wird beim erstellen eines neuen Skills nicht übernommen.|TASK.EDIT, STUDENT.WORK|
|WHICH-REQUIRED|ERR-HANDLE|Wenn benötigte Felder in der Aufgabenerstellung ausgelassen werden, so zeigt die Fehlermeldung nicht direkt, welche Felder noch gefüllt werden müssen, sondern nur, dass Eingaben fehlen.|TASK.EDIT|
|SKILLS-VALIDATION|ERR-PREV|Bei der Erstellung neuer Skills wird keine Validierung vorgenommen.|MANAGE.SKILLS|
|REQUIRED|ERR-PREV|Benötigte Felder in der Aufgabenerstellung werden nicht vorher gekennzeichnet.|TASK.EDIT|
|HOVER|HELP|Es fehlen des Öfteren Hover-Texte|\*, bspw. TASK.* für Icon-Buttons|
|DASH-REDUNDANT|RELEV|Dashboardbuttons führen immer zum selben, wenn man nicht eingeloggt ist. Die nicht funktionalen Buttons sind nicht notwendig.|DASH1|
|EMPTY-TIMELINE|RELEV|Leere Timeline, leere Kenntnisse etc. werden angezeigt, ohne Mehrwert zu erbringen.|STUDENT.UNI|
|EXPIRED-TASKS|UPTODATE, ERR-PREV|Zeitlich abgelaufene Aufgaben wurden als verfügbar angezeigt, auch wenn sie dezent als abgelaufen gekennzeichnet waren.|TASK.*|
Table: Kosmetische Probleme (einstimmig) {#tbl:cosmetical-problems}



All diese Probleme können sehr simpel und ohne die Veränderung von bestehenden Prozessen bearbeitet werden und stellen eine Liste von Problemen entsprechend Ziel Nr. 1 dar. 



### Fazit

Obgleich der Umfang der in der heuristischen Evaluation gefunden Probleme sehr groß war, konnte hier eine Teilmenge dieser als unmittelbar interessant für die weitere Betrachtung in der Arbeit charakterisiert werden.

Für die weitere Untersuchung in den Nutzertests haben sich hier der Umgang mit Fehlern nach den Heuristiken ERR-PREV, ERR-HANDLE und UNDO aufgrund ihrer problematischen und wenig umstrittenen Natur herauskristallisiert. Dabei sollte aufmerksam auch auf Probleme entsprechend der Heuristiken RELEV und CONTROL geachtet werden, welche noch problematischer, aber auch umstrittener waren. Auch wurden in +@tbl:critical-problems besonders kritische Probleme aufgeführt, welche sich zu großen Teilen in den Studentenprofilen wiederfinden. Diese Profile sollten deshalb der Kern der Nutzertests sein und der Design-Bestrebungen sein.

Für eine Implementierung von positiv wirkenden Veränderungen ohne grobe Änderungen am Design wurde besonders +@tbl:cosmetical-problems herausgearbeitet.



## Reflexion der Methodik

Die anwendete Methodik hat anhand dieser Anwendung zu einer Fülle an Ergebnissen geführt und war so durchaus erfolgreich und es konnten entsprechend der definierten Ziele sowohl Problemfelder für eine weitere Untersuchung in den Nutzertests, als auch eine Menge an eher trivialen Problemen, welche direkt Designveränderungen oder Implementierungsänderungen dienen könnten. Ebenfalls hat sich die geringe Pflege des Produktivsystems bestätigt, die es nun zu untersuchen gilt.

Ein großes Problem dieser Methodik ist der erhöhte Aufwand, welche durch die Aggregation des Textmaterials in Probleme, welche keine Redundanz aufweisen, entsteht. Auch die Diskussion der gesammelten Problemfunde erhöhte diesen. Eine gemeinsame Bewertung hätten diesen Aufwand womöglich direkt in der Analyse verringert, doch vermutlich auch eine  weniger Unvoreingenommene und individuelle Bewertung hervorgerufen. Deshalb wurde die präsentierte Methodik gewählt.

Des Weiteren kam es zu Missverständnissen bezüglich der Bedeutung der Heuristiken, weshalb diese erneut geklärt und Teile der Analyse wiederholt werden mussten um eine Vergleichbarkeit zu ermöglichen. Hierin ist eine Schwäche der heuristischen Analyse, besonders mit mehreren Evaluatoren, zu sehen. Auch kann trotz der Maßnahmen zur Reduktion des Einflusses der subjektiven Ansichten der Evaluatoren keine Garantie für die Objektivität der Problemfunde gegeben werden. Hierbei ist eine Schwäche und Stärke zugleich, dass zwei der Evaluatoren bereits breite Vorkenntnisse durch ihre Mitarbeit in der Entwicklung der Anwendung hatten. Dadurch können sie sich als Experten bereits tiefer in die Anforderungen der Anwendung hineinversetzen, allerdings besteht auch das Risiko, dass sie durch ihre enge Involvierung mit dem Projekt bereits blind gegenüber einem Teil der existierenden Probleme geworden sind und es ihnen schwieriger fällt, sich in einen neuen Nutzer hineinzuversetzen. Dies ist jedoch in diesem Verfahren weniger drastisch als es z.B. in Walkthrough-Verfahren wäre.

Ein weiteres Problem der Methodik ist der verstärkte Einsatz der Quantifizierung der Problemfunde in der Auswertung. Diese ist sehr hilfreich im Umgang mit der beachtlichen Problemmenge, aber auch problematisch, da die genutzten Metriken in ihrer Bestimmung auf mehreren subjektiven Einschätzungen fußten und des Weiteren in ihrer Art nicht unbedingt vergleichbar sind, zumal die Fundorte nur begrenzt Teil der Auswertung und kein Teil der Gewichtung eines Problems waren. Besonders offensichtlich wurde dies in der Betrachtung des Kriteriums UNDO, welches lediglich mit einem Problem beschrieben wurde, aber dennoch ein sehr wichtiges Problem darstellen kann. Hier wurde dementsprechende auf den qualitativen Unterschied aufmerksam gemacht.

Auch die Definition der Gewichtungen selbst ist schwierig und kann aufgrund von Uneindeutigkeiten zu Missverständnissen führen. Sie waren hier auf die Ziele der Analyse zugeschnitten, aber die Unterscheidung von "eindeutig nutzerunfreundliche Elemente" von zu untersuchenden Problemfeldern ist nicht unproblematisch.

Weiterhin können in diesem begrenzten Rahmen nicht alle Ergebnisse weiterverarbeitet werden - dies spricht allerdings gleichzeitig für die Menge an gefundenen Problemen. Für eine detailliertere,  tiefere Analyse des gesamten Problembestandes, wäre jedoch nicht die Wahl einer anderen Methode, sondern vielmehr die Wahl eines kleineren Teilgebiets der Anwendung notwendig gewesen. Hier erfolgt stattdessen zur Demonstration der Methodik eine Einschränkung auf Teilgebiete der Problematik.
