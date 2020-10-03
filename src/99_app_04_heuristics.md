## Heuristik-Beschreibungen {#sec:heuristik-beschreibungen}

### Heuristiken nach Shneiderman{#sec:heuristiken-shneiderman}

Die folgenden Heuristiken nach Shneiderman wurden aus [@heur:shneiderman] übernommen.

1. **Strive for consistency.**
   Consistent sequences of actions should be required in similar situations; identical terminology should be used in prompts, menus, and help screens; and consistent color, layout, capitalization, fonts, and so on, should be employed throughout. Exceptions, such as required confirmation of the delete command or no echoing of passwords, should be comprehensible and limited in number
2. **Seek universal usability.**
   Recognize the needs of diverse users and design for plasticity, facilitating transformation of content. Novice to expert differences, age ranges, disabilities, international variations, and technological diversity each enrich the spectrum of requirements that guides design. Adding features for novices, such as explanations, and features for experts, such as shortcuts and faster pacing, enriches the interface design and improves perceived quality.

3. **Offer informative feedback.**
   For every user action, there should be an interface feedback. For frequent and minor actions, the response can be modest, whereas for infrequent and major actions, the response should be more substantial. Visual presentation of the objects of interest provides a convenient environment for showing changes explicitly (see the discussion of direct manipulation in Chapter 7).

4. **Design dialogs to yield closure.**
   Sequences of actions should be organized into groups with a beginning, middle, and end. Informative feedback at the completion of a group of actions gives users the satisfaction of accomplishment, a sense of relief, a signal to drop contingency plans from their minds, and an indicator to prepare for the next group of actions. For example, e-commerce websites move users from selecting products to the checkout, ending with a clear confirmation page that completes the transaction.

5. **Prevent errors.**
   As much as possible, design the interface so that users cannot make serious errors; for example, gray out menu items that are not appropriate and do not allow alphabetic characters in numeric entry fields (Section 3.3.5). If users make an error, the interface should offer simple, constructive, and specific instructions for recovery. For example, users should not have to retype an entire name-address form if they enter an invalid zip code but rather should be guided to repair only the faulty part. Erroneous actions should leave the interface state unchanged, or the interface should give instructions about restoring the state.

6. **Permit easy reversal of actions.**
   As much as possible, actions should be reversible. This feature relieves anxiety, since users know that errors can be undone, and encourages exploration of unfamiliar options. The units of reversibility may be a single action, a data-entry task, or a complete group of actions, such as entry of a name-address block.

7. **Keep users in control.**
   Experienced users strongly desire the sense that they are in charge of the interface and that the interface responds to their actions. They don’t want surprises or changes in familiar behavior, and they are annoyed by tedious data-entry sequences, difficulty in obtaining necessary information, and inability to produce their desired result.

8. **Reduce short-term memory load.**
   Humans’ limited capacity for information processing in short-term memory (the rule of thumb is that people can remember “seven plus or minus two chunks” of information) requires that designers avoid interfaces in which users must remember information from one display and then use that information on another display. It means that cellphones should not require reentry of phone numbers, website locations should remain visible, and lengthy forms should be compacted to fit a single display.

### Heuristiken nach Nielsen{#sec:heuristiken-nielsen}

Die folgenden Heuristiken nach Nielsen wurden aus [@heur:nielsen] übernommen.

1. **Visibility of system status**
   The system should always keep users informed about what is going on, through appropriate feedback within reasonable time. 
2. **Match between system and the real world**
   The system should speak the users' language, with words, phrases and concepts familiar to the user, rather than system-oriented terms. Follow real-world conventions, making information appear in a natural and logical order. 
3. **User control and freedom**
   Users often choose system functions by mistake and will need a clearly marked "emergency exit" to leave the unwanted state without having to go through an extended dialogue. Support undo and redo.
4. **Consistency and standards**
   Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform conventions.
5. **Error prevention**
   Even better than good error messages is a careful design which prevents a problem from occurring in the first place. Either eliminate error-prone conditions or check for them and present users with a confirmation option before they commit to the action.
6. **Recognition rather than recall**
   Minimize the user's memory load by making objects, actions, and options visible. The user should not have to remember information from one part of the dialogue to another. Instructions for use of the system should be visible or easily retrievable whenever appropriate.
7. **Flexibility and efficiency of use**
   Accelerators -- unseen by the novice user -- may often speed up the interaction for the expert user such that the system can cater to both inexperienced and experienced users. Allow users to tailor frequent actions. 
8. **Aesthetic and minimalist design**
   Dialogues should not contain information which is irrelevant or rarely needed. Every extra unit of information in a dialogue competes with the relevant units of information and diminishes their relative visibility.
9. **Help users recognize, diagnose, and recover from errors** 
   Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution. 
10. **Help and documentation**
    Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation. Any such information should be easy to search, focused on the user's task, list concrete steps to be carried out, and not be too large.



### Vereinigungsverfahren der Kriterien {#sec:heur-merge}

| Nielsen                                                 |           Extrahiertes Kriterium            |                      Shneiderman |
| :------------------------------------------------------ | :-----------------------------------------: | -------------------------------: |
| Match between system and the real world                 |    Realitätsnahe Semantik und Vokabular     |                                  |
| Aesthetic and minimalist design                         |         Relevanz der Kommunikation          |                                  |
| Help users recognize, diagnose, and recover from errors |        Konstruktive Fehlerbehandlung        |                                  |
| Help and documentation                                  |           Hilfe und Dokumentation           |                                  |
|                                                         |                                             |                                  |
|                                                         |           Abgeschlossene Aktionen           | Design dialogs to yield closure. |
|                                                         |         Benutzerbestimmte Eingaben          |           Keep users in control. |
|                                                         |                                             |                                  |
| User control and freedom                                |    Reversibilität und Abbruchmöglichkeit    | Permit easy reversal of actions. |
| Visibility of system status                             | Sichtbarer Systemstatus und Statusmeldungen |      Offer informative feedback. |
| Consistency and standards                               |        Konsistenz und Standardtreue         |          Strive for consistency. |
| Error prevention                                        |              Fehlerprävention               |                  Prevent errors. |
| Recognition rather than recall                          |            Erkennen vor Erinnern            |   Reduce short-term memory load. |
| Flexibility and efficiency of use                       | Universelle Benutzbarkeit und Anpassbarkeit |        Seek universal usability. |

Table: Herleitung der Kriterien der Heuristischen Evaluation {#tbl:mergecriteria}



## Rohergebnisse der Heuristischen Evaluation {#sec:heuristik-rohergebnisse}

### Problemfunde je Evaluator

#### Hans

| Kriterium                 | Problem                                                      | Fundort              |
| ------------------------- | ------------------------------------------------------------ | -------------------- |
| ADAPT                     | Kontraste im dunklen Modus sind häufig schlecht, Beispiele dafür sind der Dark-Mode-Schalter selbst, Lade-Spinner oder die Kennzeichnung aktuell ausgewählter Tabs. | *                    |
| ADAPT                     | Viele UI-Elemente basieren pur auf Icons ohne Schrift, selbst ohne Hovertexte. Das ist für Nutzer, die nicht mit der Symbolik vertraut sind, oder sich aufgrund körperlicher Einschränkungen auf Screenreader verlassen, ein Erschwernis. (Z.B. häufig hinzufügen, editieren, etc.) | z.B. TASKS.*         |
| ADAPT                     | Es gibt keine Anpassungsmöglichkeiten außerhalb des Farbschemas, der Nutzer kann zum Beispiel Layouts, graphische Optionen oder ähnliches nicht an sich anpassen. | *                    |
| ADAPT                     | Es existieren keine beschleunigenden Features für Experten. Es existieren allgemein keine Tastaturkürzel für Aktionen. | *                    |
| ADAPT                     | Bei abweichender Bildschirmgröße sind Inhalte häufig außerhalb des initialen Bildschirms und es muss gescrollt werden und die Anwendung ist nicht für mobile Anwendungen optimiert. | *                    |
| CLOSURE                   | Das Speichern von Credit Points gibt wenig Feedback bei der Bestätigung der Eingabe. Insgesamt ist es schwer ersichtlich, dass man die Eingabe noch manuell abschließen muss, der Prozess ist nicht atomar. | STUDENT.UNI          |
| CLOSURE/STATUS            | Feedback zu erfolgreichen Aktionen teilweise schwer mitzubekommen oder gar nicht existent. (z.B. Kenntnisse speichern) | STUDENT.WORK         |
| CONSIST                   | FAQ und Dateinamen verwenden eine andere Schriftart als der Rest der Anwendung. | FAQ, STUDENT.UNI     |
| CONSIST                   | Einige GUI-Elemente, sind speziell für die Anwendung entwickelt worden und sind nicht direkt intuitiv, sondern leicht verwirrend. (z.B. das Widget zur Bearbeitung der Credit-Points) | STUDENT.UNI          |
| CONSIST                   | Der Slider für Skills startet nicht ganz links und endet nicht ganz rechts. Dies ist leicht irritierend, da man vermuten kann, ein Bedienungsfehler wäre aufgetreten. | STUDENT.WORK         |
| CONTROL                   | Die Verfügbarkeitssicht startet am Beginn der Aufzeichnung und nicht an einem vom Nutzer bestimmten Punkt bzw. am heutigen Datum. Es muss jedes Mal mühselig vorgescrollt werden. | STUDENT.WORK         |
| CONTROL                   | Die Suchfilter sind nicht sofort verständlich in ihrer Bedeutung. Sie setzen sich bei einer neuen Sucheingabe zurück. | SEARCH               |
| CONTROL                   | Ein Klick auf einen Skill führt ohne Vorwarnung oder Kennzeichnung eine Weiterleitung auf externe Websites, welche von Nutzern angegeben werden. | TASK.VIEW            |
| CONTROL                   | Eingetragene TFLs können nicht editiert, sondern nur neu angelegt werden. | STUDENT.UNI          |
| ERR-HANDLE                | Wenn benötigte Felder in der Aufgabenerstellung ausgelassen werden, so zeigt die Fehlermeldung nicht direkt, welche Felder noch gefüllt werden müssen, sondern nur, dass Eingaben fehlen. | TASK.EDIT            |
| ERR-HANDLE                | Bei einem provozierten Fehler wurde kontinuierlich gespeichert, ein Abbrechen war nicht möglich oder keine Fehlermeldung wurde angezeigt. (Hochladen von Dateien) | STUDENT.UNI.NEW-TFL  |
| ERR-HANDLE / STATUS       | Bei dem Versuch der Erstellung einer Hochschule ohne Namen kommt ein intransparenter, langer Ladevorgang ohne anschließende Misserfolgsmeldung. | MANAGE.UNI           |
| ERR-PREV                  | Benötigte Felder in der Aufgabenerstellung werden nicht vorher gekennzeichnet. | TASK.EDIT            |
| ERR-PREV                  | Kein Nachfragen wenn geänderte Aufgabe nicht gespeichert und dann abgebrochen wird | TASK.EDIT            |
| ERR-PREV                  | Notwendige Felder beim Anlegen von Aufgaben erst im Nachhinein angezeigt | TASK.EDIT            |
| ERR-PREV                  | Aktionsbuttons werden häufig mit Aktionen wie "ok" betitelt, eine sprechende Bezeichnung der Aktion, die folgt, wäre besser. | *                    |
| ERR-PREV                  | Bei editierten Credit Points oder Kenntnissen im Profil keine Nachfrage beim Verlassen der Seite | STUDENT.WORK         |
| HELP                      | Kaum nützliche Hover-Texte.                                  | *                    |
| HELP                      | Kein abrufbarer Hilfe-Dialog, FAQ ist dürftig.               | FAQ                  |
| HELP                      | Es ist nicht immer klar beschrieben, welche Konsequenzen eine Aktion hat. | *                    |
| REAL                      | Alumni & Alumnae ist ein selten verwendeter Begriff, neue Studenten können damit vielleicht nicht viel anfangen. | STUDENT.LIST         |
| REAL                      | Icons für offene / angefangen Aufgaben sind unbekannt und transportieren keine klare Nachricht. | TASK.VIEW            |
| REAL                      | Die Bezeichnungen der Aufgabenkategorien haben keine klare Beziehung zum echten Leben. Wie lange dauern Einzel- vs. Daueraufgaben? Warum werden nur offene Aufgaben angezeigt? Wo ist das Archiv? (AW: in "Alle Aufgaben") | TASK.*               |
| RECOG                     | Es ist z.B. nicht mehr klar, welches Profil gerade editiert wird, wenn ein Editierdialog offen ist. | STUDENT.*            |
| RECOG / STATUS / ERR-PREV | Nicht abzusehen ob eine editierte Aufgabe,CP,Kenntnisse bereits gespeichert oder noch "dirty" ist. | STUDENT.*            |
| RELEV                     | Die potentiell etwas längere Kurzbeschreibung bläht das Layout auf. Der Titel würde hier reichen. | STUDENT.UNI          |
| RELEV                     | Credit Points werden auch dann angezeigt, wenn keine Daten vorhanden sind (auch auf fremden Profilen) | STUDENT.UNI          |
| RELEV                     | Leere Timeline, leere Kenntnisse etc. werden angezeigt, ohne Mehrwert zu erbringen. | STUDENT.UNI          |
| RELEV                     | Aufgaben können nicht nach (eigenen) Kenntnissen  gefiltert werden | TASK.*, SEARCH       |
| RELEV                     | Zu jedem Studenten wird zusätzlich ein unnützes Nutzerkürzel angezeigt. | STUDENT.*, MANAGE.\* |
| STATUS                    | Es gibt keinen schnellen Indikator für den eingeloggten Benutzer. | *                    |
| STATUS                    | Es ist leicht zu übersehen, dass das Editieren von CP noch aktiv ist. | STUDENT.UNI          |
| UNDO                      | Keine Möglichkeit, Änderungen rückgängig zu machen oder auch nur nachzuverfolgen | *                    |
| UPTODATE / ERR-PREV       | Zeitlich abgelaufene Aufgaben wurden als verfügbar angezeigt, auch wenn sie dezent als abgelaufen gekennzeichnet waren. | TASK.*               |
| UPTODATE / ERR-PREV       | Es existieren unmögliche Nutzerdaten, wie zum Beispiel ein Nutzer, der seit 2017 Student, aber im 2. Semester ist, oder noch gravierender seit 2021 aber Student aber im 20. Semester. Hier fehlen Validierungen. | STUDENT.*            |

Table: Problemfunde Hans {#tbl:heur:hans}



#### Hendrik

| Kriterium          | Probleme                                                     | Fundort                           |
| ------------------ | ------------------------------------------------------------ | --------------------------------- |
| ADAPT              | Kontraste im Darkmode sind nicht gut, Elemente könnten übersehen werden. | MANAGE, TASK.*, FAQ, STUDENT.WORK |
| CLOSURE            | Bei Bearbeitung des Studentenprofils ist der Abschluss von Aufgaben nicht klar, es kann ewig ohne klare Abfolge editiert werden. | STUDENT.UNI, STUDENT.WORK         |
| CLOSURE            | Das Verändern der Kenntnisse ruft keine Speicheroperation hervor und durch eine Speicheroperation wird keine Rückmeldung hervorgerufen, die die Aktion für den Nutzer abschließt | STUDENT.WORK                      |
| CONSIST            | Die Webseite verwendet kein HTTPS, wodurch potentiell Unsicherheit entsteht. | *                                 |
| CONSIST            | Aufgabenstatus sind auf Englisch, wenn der Rest der Anwendung auf Deutsch ist | TASK.*                            |
| CONSIST            | Studenten in den Aufgaben sehen aus, als könnte man sie anklicken, aber nichts passiert  danach | TASK.VIEW                         |
| CONSIST            | Kenntnisse sehen beim Anlegen einer Aufgabe aus als wären sie anklickbar. | TASK.EDIT                         |
| CONTROL            | Die "Verfügbarkeit"-Zeitlinie ist nicht auf das aktuelle Datum gerichtet. | STUDENT.UNI                       |
| CONTROL            | Es können nicht alle wissenschaftlichen Arbeiten auf einmal gesucht / gefunden werden. | *                                 |
| CONTROL / RECOG    | Beim Anlegen eines neuen Kalendereintrags sind Aufgaben schwer auffindbar und können nicht neu angelegt werden. Der Nutzer muss sich den Namen der Aufgabe gemerkt haben. | STUDENT.WORK.NEW-ENTRY            |
| ERR-PREV           | Bei der Erstellung neuer Skills wird keine Validierung vorgenommen. | MANAGE.SKILLS                     |
| ERR-PREV / CONTROL | Ich weiß nicht, was für eine Mail versendet wird, wenn ich auf Interesse drücke. | TASK.VIEW                         |
| HELP               | Bei Skills ist nicht klar, bei welchem Skill ich mich selber einordnen soll, es existiert keine Dokumentation als Vergleichsreferenz. | STUDENT.WORK                      |
| HELP               | Das FAQ ist nicht wirklich gut.                              | FAQ                               |
| REAL               | Dauer-/Einzelaufgaben sind keine Worte aus der realen Welt, und sollen eher Aufgaben vs. Teams darstellen. | TASK.SINGLE, TASK.PERM            |
| REAL               | Creditpoints für "Hausarbeiten" stimmen nicht überein, da z.B. für NAK-Studenten hier TFLs gemeint sind. | STUDENT.UNI                       |
| RELEV              | Dashboardbuttons führen immer zum selben, wenn man nicht eingeloggt ist. Die nicht funktionalen Buttons sind nicht notwendig. | DASH1                             |
| STATUS             | Die Veränderung der Rolle eines Nutzers zieht keine Erfolgsmeldung nach sich. | MANAGE.USER                       |
| UNDO               | Ein Undo/Redo ist nicht möglich                              | *                                 |
| UPTODATE           | Keine Aufgaben sind im Startbereich zu sehen                 | TASK.ALL                          |
| UPTODATE           | Ehemalige Studenten werden als Studenten geführt.            | STUDENT.LIST                      |
| UPTODSATE          | Profile sind wenig gepflegt.                                 | STUDENT.*                         |
| UPTODATE           | Standort von Aufgabe ist schlecht dokumentiert.              | TASK.*                            |
| UPTODATE           | Semesterangaben sind bei einigen Studenten um ein Semester versetzt. | STUDENT.UNI                       |

Table: Problemfunde Hendrik {#tbl:heur:hendrik}



#### Til

| Kriterium       | Probleme                                                     | Fundort                   |
| --------------- | ------------------------------------------------------------ | ------------------------- |
| ADAPT           | Keine Anpassbarkeit vorhanden.                               | *                         |
| CONSIST         | Keine expliziten Speicher-Buttons an einigen Orten, an anderen schon. | STUDENT.*, MANAGE.\*      |
| CONSIST         | Layout (Spacings etc.) ist teilweise uneinheitlich.          | TASK.*                    |
| CONSIST         | Vertikale / Horizontale Einrückung nicht gleichmäßig / einheitlich in der Anwendung. | *                         |
| CONSIST         | Teilweise geringer Kontrast im Dark Mode.                    | *                         |
| CONSIST         | Layout von Suchergebnissen ist nicht einheitlich.            | SEARCH                    |
| CONSIST         | Kein Such-Button, wenn ein vorherige Query noch drin steht   | SEARCH                    |
| CONSIST         | Suchfeld wird von Passwort Managern als Password Feld erkannt | SEARCH                    |
| CONTROL         | Suchergebnis wird beim erstellen eines neuen Skills nicht übernommen. | TASK.EDIT, STUDENT.WORK   |
| CONTROL         | Einsatze können nicht direkt gelöscht werden                 | STUDENT.WORK              |
| CONTROL / ADAPT | Neuanordnung von Einsätzen ist nicht einfach möglich         | STUDENT.WORK              |
| CONTROL / RECOG | Bei Einsätzen können nur existierende Aufgaben eingetragen werden. | STUDENT.WORK              |
| ERR-HANDLE      | Keine Fehlermeldung beim Scheitern des Hochladens von TFLs   | STUDENT.UNI               |
| ERR-PREV        | Der "Speichern"-Button / -Prozess ist nicht offensichtlich und kann übersehen werden. | STUDENT.WORK              |
| ERR-PREV        | Wenn man eine Kenntnis verändert, nicht speichert und dann eine neue Kenntnis hinzufügt dann werden die Änderungen an der ersten Kenntnis verworfen. | STUDENT.WORK              |
| ERR-PREV        | Wenn während des Editierens per Navigation die Seite gewechselt wird, werden Änderungen nicht gespeichert und es erfolgt keine Warnung. | TASK.EDIT                 |
| HELP            | FAQ ist vorhanden, Inhalt ist in Ordnung aber der Umfang ist zu gering. | FAQ                       |
| HELP            | Teilweise Tooltips vorhanden, teilweise aber auch nicht (z.B. Icon-Buttons wie Editieren oder Löschen). | z.B. TASK.* oder MANAGE.* |
| REAL            | Einzelaufgaben vs. Daueraufgaben ist nicht sinnvoll          | TASK.SINGLE, TASK.PERM    |
| REAL            | "Deine" Aufgaben ist irreführend, da hier eingestellte Aufgaben aufgeführt sind und nicht die, die ein User bearbeitet. | TASK.YOUR                 |
| RELEV           | Die genaue Anzahl von Credit Points sind schwer zu pflegen und liefern vermutlich keinen sinnvollen Nutzen. | STUDENT.UNI               |
| RELEV           | Die Informationsdichte ist zu gering                         | TASK.VIEW                 |
| RELEV           | Die Suche nach Kenntnissen ist **zu** "fuzzy" und zeigt sehr viele irrelevante Ergebnisse an, auch wenn lieber eine neue Kenntnis erstellt werden soll. | TASK.EDIT, STUDENT.WORK   |
| RELEV           | Teilweise sind unnütze UI Elemente vorhanden. (z.B. Labels "Kenntnisse" oder "Standort", obwohl dort keine Daten hinterlegt sind.) | TASK.VIEW                 |
| UNDO            | UNDO nicht möglich und keine Nachvollziehbarkeit             | *                         |
| UPTODATE        | Die Nutzerprofile sind nicht aktuell.                        | STUDENT.*                 |
| UPTODATE        | Es sind wenige Daten zu Transferleistungen verfügbar.        | STUDENT.UNI               |

Table: Problemfunde Til {#tbl:heur:til}

### Gemeinsame Ergebnisliste

|      Bezeichner      |        Kriterium        |                         Beschreibung                         |                         Fundorte                          |  G   | $\Delta$ |
| :------------------: | :---------------------: | :----------------------------------------------------------: | :-------------------------------------------------------: | :--: | :------: |
|    RESPON-SIVITY     |          ADAPT          | Bei abweichender Bildschirmgröße sind Inhalte häufig außerhalb des initialen Bildschirms und es muss gescrollt werden und die Anwendung ist nicht für mobile Anwendungen optimiert. |                             *                             |  1   |    2     |
|    ACCELE-RATORS     |          ADAPT          | Es existieren keine beschleunigenden Features für Experten. Es existieren allgemein keine Tastaturkürzel für Aktionen. |                             *                             |  1   |    0     |
|       SETTINGS       |          ADAPT          |      Keine Einstellungen oder Anpassungsmöglichkeiten.       |                             *                             |  1   |    2     |
|        ICONS         |          ADAPT          | Viele UI-Elemente basieren pur auf Icons ohne Schrift oder Hovertexte. Das ist für Nutzer, die nicht mit der Symbolik vertraut sind, oder sich aufgrund körperlicher Einschränkungen auf Screenreader verlassen, ein Erschwernis. |       z.B. TASKS.*  (häufig hinzufügen, editieren)        |  2   |    2     |
|         DARK         |     ADAPT, CONSIST      |               Schlechte Kontraste im Darkmode.               | MANAGE, TASK.*, FAQ, STUDENT.WORK, Lade-Indikatoren,Tabs, |  2   |    0     |
|   ENDLESS-PROFILE    |         CLOSURE         | Bei Bearbeitung des Studentenprofils ist der Abschluss von Aufgaben nicht klar, es kann ewig ohne klare Abfolge editiert werden. |                 STUDENT.UNI, STUDENT.WORK                 |  3   |    0     |
|     CP-FEEDBACK      |         CLOSURE         | Das Speichern von Credit Points gibt wenig Feedback bei der Bestätigung der Eingabe. Insgesamt ist es schwer ersichtlich, dass man die Eingabe noch manuell abschließen muss, der Prozess ist nicht atomar. |                        STUDENT.UNI                        |  3   |    0     |
|     SKILLS-SAVED     |     CLOSURE, STATUS     | Das Verändern der Kenntnisse ruft keine Speicheroperation hervor und durch eine Speicheroperation wird keine Rückmeldung hervorgerufen, die die Aktion für den Nutzer abschließt |                       STUDENT.WORK                        |  3   |    0     |
|    ENGLISH-STATUS    |         CONSIST         | Aufgabenstatus sind auf Englisch, wenn der Rest der Anwendung auf Deutsch ist |                          TASK.*                           |  1   |    0     |
|        SLIDER        |         CONSIST         | Der Slider für Skills startet nicht ganz links und endet nicht ganz rechts. Dies ist leicht irritierend, da man vermuten kann, ein Bedienungsfehler wäre aufgetreten. |                       STUDENT.WORK                        |  2   |    4     |
|        HTTPS         |         CONSIST         | Die Webseite verwendet kein HTTPS, wodurch potentiell Unsicherheit entsteht. |                             *                             |  1   |    4     |
|      CUSTOM-UI       |         CONSIST         | Einige GUI-Elemente, sind speziell für die Anwendung entwickelt worden und sind nicht direkt intuitiv, sondern leicht verwirrend. (z.B. das Widget zur Bearbeitung der Credit-Points) |                        STUDENT.UNI                        |  2   |    2     |
|         FONT         |         CONSIST         | FAQ und Dateinamen verwenden eine andere Schriftart als der Rest der Anwendung. |                     FAQ, STUDENT.UNI                      |  1   |    2     |
|    SEARCH-BUTTON     |         CONSIST         |  Kein Such-Button, wenn ein vorherige Query noch drin steht  |                          SEARCH                           |  3   |    4     |
|     SAVE-CONCEPT     |         CONSIST         | Keine expliziten Speicher-Buttons an einigen Orten, an anderen schon. |                   STUDENT.\*, MANAGE.\*                   |  3   |    2     |
|     CLICK-SKILLS     |         CONSIST         | Kenntnisse sehen beim Anlegen einer Aufgabe aus als wären sie anklickbar. |                         TASK.EDIT                         |  2   |    2     |
|       SPACING        |         CONSIST         |     Layout (Spacings etc.) ist teilweise uneinheitlich.      |                          TASK.*                           |  2   |    2     |
|       OFFSETS        |         CONSIST         | Vertikale und Horizontale Einrückungen sind nicht einheitlich |                             *                             |  2   |    2     |
|    SEARCH-LAYOUT     |         CONSIST         |      Layout von Suchergebnissen ist nicht einheitlich.       |                          SEARCH                           |  2   |    0     |
|    CLICK-STUDENTS    |         CONSIST         | Studenten in den Aufgaben sehen aus, als könnte man sie anklicken, aber nichts passiert danach |                         TASK.VIEW                         |  1   |    2     |
|   SEARCH-PASSWORD    |         CONSIST         | Suchfeld wird von Passwort Managern als Password Feld erkannt |                          SEARCH                           |  3   |    4     |
|     FILTER-RESET     |         CONTROL         | Die Suchfilter sind nicht sofort verständlich in ihrer Bedeutung. Sie setzen sich bei einer neuen Sucheingabe zurück. |                          SEARCH                           |  3   |    2     |
|       TIMELINE       |         CONTROL         | Die Verfügbarkeitssicht startet am Beginn der Aufzeichnung und nicht an einem vom Nutzer bestimmten Punkt bzw. am heutigen Datum. Es muss jedes Mal mühselig vorgescrollt werden. |                       STUDENT.WORK                        |  3   |    2     |
|  EXTERNAL-WEBSITES   |         CONTROL         | Ein Klick auf einen Skill führt ohne Vorwarnung oder Kennzeichnung eine Weiterleitung auf externe Websites, welche von Nutzern angegeben werden. |                         TASK.VIEW                         |  2   |    2     |
|       TFL-EDIT       |         CONTROL         | Eingetragene TFLs können nicht editiert, sondern nur neu angelegt werden. |                        STUDENT.UNI                        |  3   |    0     |
|   DELETE-CALENDAR    |         CONTROL         |         Einsatze können nicht direkt gelöscht werden         |                       STUDENT.WORK                        |  3   |    2     |
|       ALL-TFLS       |         CONTROL         | Es können nicht alle wissenschaftlichen Arbeiten auf einmal gesucht / gefunden werden. |                             *                             |  3   |    4     |
|  NEW-SKILL-REENTRY   |         CONTROL         | Suchergebnis wird beim erstellen eines neuen Skills nicht übernommen. |                  TASK.EDIT, STUDENT.WORK                  |  2   |    0     |
|   REORDER-CALENDAR   |     CONTROL, ADAPT      |     Neuanordnung von Einsätzen ist nicht einfach möglich     |                       STUDENT.WORK                        |  1   |    6     |
|  TASK-FOR-CALENDAR   |     CONTROL, RECOG      | Beim Anlegen eines neuen Kalendereintrags sind Aufgaben schwer auffindbar und können nicht neu angelegt werden. Der Nutzer muss sich den Namen der Aufgabe gemerkt haben. |                  STUDENT.WORK.NEW-ENTRY                   |  3   |    0     |
| NO-ERROR-TFL-UPLOAD  |       ERR-HANDLE        | Bei einem provozierten Fehler wurde kontinuierlich gespeichert, ein Abbrechen war nicht möglich oder keine Fehlermeldung wurde angezeigt. (Hochladen von Dateien) |                    STUDENT.UNI.NEW-TFL                    |  3   |    0     |
|    WHICH-REQUIRED    |       ERR-HANDLE        | Wenn benötigte Felder in der Aufgabenerstellung ausgelassen werden, so zeigt die Fehlermeldung nicht direkt, welche Felder noch gefüllt werden müssen, sondern nur, dass Eingaben fehlen. |                         TASK.EDIT                         |  2   |    0     |
|      OK-BUTTON       |        ERR-PREV         | Aktionsbuttons werden häufig mit Aktionen wie "ok" betitelt, eine sprechende Bezeichnung der Aktion, die folgt, wäre besser. |                             *                             |  1   |    2     |
|  SKILLS-VALIDATION   |        ERR-PREV         | Bei der Erstellung neuer Skills wird keine Validierung vorgenommen. |                       MANAGE.SKILLS                       |  2   |    0     |
| DIRTY-PROFILE-LEAVE  |        ERR-PREV         | Bei editierten Credit Points oder Kenntnissen im Profil keine Nachfrage beim Verlassen der Seite |                       STUDENT.WORK                        |  3   |    0     |
|       REQUIRED       |        ERR-PREV         | Benötigte Felder in der Aufgabenerstellung werden nicht vorher gekennzeichnet. |                         TASK.EDIT                         |  2   |    0     |
|   CANCEL-TASK-EDIT   |        ERR-PREV         | Kein Nachfragen wenn geänderte Aufgabe nicht gespeichert und dann abgebrochen oder die Seite verlassen wird |                         TASK.EDIT                         |  3   |    0     |
| ADD-SKILL-WITH-DIRTY |        ERR-PREV         | Wenn man eine Kenntnis verändert, nicht speichert und dann eine neue Kenntnis hinzufügt dann werden die Änderungen an der ersten Kenntnis verworfen. |                       STUDENT.WORK                        |  3   |    0     |
|     UNCLEAR-MAIL     |    ERR-PREV, CONTROL    | Ich weiß nicht, was für eine Mail versendet wird, wenn ich auf Interesse drücke. |                         TASK.VIEW                         |  1   |    4     |
|    SKILLS-UNCLEAR    |          HELP           | Bei Skills ist nicht klar, bei welchem Skill ich mich selber einordnen soll, es existiert keine Dokumentation als Vergleichsreferenz. |                       STUDENT.WORK                        |  1   |    0     |
|        HOVER         |          HELP           |              Es fehlen des Öfteren Hover-Texte               |            \*, bspw. TASK.\* für Icon-Buttons             |  2   |    0     |
|     CONSEQUENCES     |          HELP           | Es ist nicht immer klar beschrieben, welche Konsequenzen eine Aktion hat. |                             *                             |  1   |    2     |
|         FAQ          |          HELP           | FAQ ist vorhanden, Inhalt ist in Ordnung aber der Umfang ist zu gering. |                            FAQ                            |  1   |    0     |
|       ALUMNAE        |          REAL           | Alumni & Alumnae ist ein selten verwendeter Begriff, neue Studenten können damit vielleicht nicht viel anfangen. |                       STUDENT.LIST                        |  1   |    2     |
|      TASK-TABS       |          REAL           | Die Bezeichnungen der Aufgabenkategorien haben keine klare Beziehung zum echten Leben. Wie lange dauern Einzel- vs. Daueraufgaben? Warum werden nur offene Aufgaben angezeigt? Wo ist das Archiv? (AW: in "Alle Aufgaben") |                          TASK.*                           |  2   |    2     |
|   MISLEADING-YOUR    |          REAL           | Deine Aufgaben ist irreführend, da hier eingestellte Aufgaben aufgeführt sind und nicht die, die ein User bearbeitet. |                         TASK.YOUR                         |  2   |    4     |
|      CP-MEANING      |          REAL           | Creditpoints für "Hausarbeiten" stimmen nicht überein, da z.B. für NAK-Studenten hier TFLs gemeint sind. |                        STUDENT.UNI                        |  1   |    0     |
|   TASK-STATUS-ICON   |          REAL           | Icons für offene / angefangen Aufgaben sind unbekannt und transportieren keine klare Nachricht. |                         TASK.VIEW                         |  2   |    2     |
|    WHICH-PROFILE     |          RECOG          | Es ist z.B. nicht mehr klar, welches Profil gerade editiert wird, wenn ein Editierdialog offen ist. |                         STUDENT.*                         |  2   |    2     |
|     UNSEEN-DIRTY     | RECOG, STATUS, ERR-PREV | Nicht abzusehen ob eine editierte Aufgabe,CP,Kenntnisse bereits gespeichert oder noch "dirty" ist. |                         STUDENT.*                         |  3   |    0     |
|    DASH-REDUNDANT    |          RELEV          | Dashboardbuttons führen immer zum selben, wenn man nicht eingeloggt ist. Die nicht funktionalen Buttons sind nicht notwendig. |                           DASH1                           |  2   |    0     |
|     SEARCH-FUZZY     |          RELEV          | Die Suche nach Kenntnissen ist zu "fuzzy" und zeigt sehr viele irrelevante Ergebnisse an, auch wenn lieber eine neue Kenntnis erstellt werden soll. |                  TASK.EDIT, STUDENT.WORK                  |  3   |    4     |
|    USELESS-LABELS    |          RELEV          | Teilweise sind unnütze UI Elemente vorhanden. (z.B. Labels "Kenntnisse" oder "Standort", obwohl dort keine Daten hinterlegt sind.) |                         TASK.VIEW                         |  2   |    2     |
|      CP-USELESS      |          RELEV          | Die genaue Anzahl von Credit Points sind schwer zu pflegen und liefern vermutlich keinen sinnvollen Nutzen. |                         TASK.VIEW                         |  3   |    4     |
|     TAKS-DENSITY     |          RELEV          |             Die Informationsdichte ist zu gering             |                  TASK.EDIT, STUDENT.WORK                  |  1   |    4     |
|   TFL-DESCRIPTION    |          RELEV          | Die potentiell etwas längere Kurzbeschreibung von wissenschaftlichen Arbeiten bläht das Layout auf. Der Titel würde hier reichen. |                        STUDENT.UNI                        |  2   |    2     |
|       EMPTY-CP       |          RELEV          | Credit Points werden auch dann angezeigt, wenn keine Daten vorhanden sind (auch auf fremden Profilen) |                        STUDENT.UNI                        |  2   |    2     |
|    EMPTY-TIMELINE    |          RELEV          | Leere Timeline, leere Kenntnisse etc. werden angezeigt, ohne Mehrwert zu erbringen. |                        STUDENT.UNI                        |  2   |    0     |
|     SKILL-FILTER     |          RELEV          | Aufgaben können nicht nach (eigenen) Kenntnissen gefiltert werden |                      TASK.*, SEARCH                       |  3   |    2     |
|    USER-SHORTCUT     |          RELEV          | Zu jedem Studenten wird zusätzlich ein unnützes Nutzerkürzel angezeigt. |                   STUDENT.\*, MANAGE.\*                   |  1   |    4     |
|  USER-ROLE-FEEDBACK  |         STATUS          | Die Veränderung der Rolle eines Nutzers zieht keine Erfolgsmeldung nach sich. |                        MANAGE.USER                        |  2   |    2     |
|      LOGGED-IN       |         STATUS          | Es gibt keinen schnellen Indikator für den eingeloggten Benutzer. |                             *                             |  1   |    2     |
|         UNDO         |          UNDO           | Keine Möglichkeit, Änderungen rückgängig zu machen oder auch nur nachzuverfolgen |                             *                             |  3   |    0     |
|     OLD-STUDENTS     |        UPTODATE         |      Ehemalige Studenten werden als Studenten geführt.       |                       STUDENT.LIST                        |  1   |    4     |
|        NO-TFL        |        UPTODATE         |    Es sind wenige Daten zu Transferleistungen verfügbar.     |                        STUDENT.UNI                        |  2   |    2     |
|       NO-TASKS       |        UPTODATE         |         Keine Aufgaben sind im Startbereich zu sehen         |                         TASK.ALL                          |  3   |    0     |
|       PROFILES       |        UPTODATE         |        Profile sind wenig gepflegt und nicht aktuell.        |                         STUDENT.*                         |  3   |    0     |
|   SEMESTERS-WRONG    |        UPTODATE         | Semesterangaben sind bei einigen Studenten um ein Semester versetzt. |                        STUDENT.UNI                        |  2   |    2     |
|       LOCATION       |        UPTODATE         |       Standort von Aufgabe ist schlecht dokumentiert.        |                          TASK.*                           |  2   |    2     |
| IMPOSSIBLE-STUDENTS  |   UPTODATE, ERR-PREV    | Es existieren unmögliche Nutzerdaten, wie zum Beispiel ein Nutzer, der seit 2017 Student, aber im 2. Semester ist, oder noch gravierender seit 2021 aber Student aber im 20. Semester. Hier fehlen Validierungen. |                         STUDENT.*                         |  2   |    2     |
|    EXPIRED-TASKS     |   UPTODATE, ERR-PREV    | Zeitlich abgelaufene Aufgaben wurden als verfügbar angezeigt, auch wenn sie dezent als abgelaufen gekennzeichnet waren. |                          TASK.*                           |  2   |    0     |

Table: Finales Ergebnis der heuristischen Analyse {#tbl:heur:final}

### Gewichtung der Evaluatoren

| Problembezeichner | Hans | Hendrik | Til  | Einigung | Abweichungen|
| :---------------------------: | :----: | :----: | :----: | :----: | :-----: |
| RESPONSIVITY         | 1            | 1               | 0           | 1          | 2            |
| ACCELERATORS         | 1            | 1               | 1           | 1          | 0            |
| SETTINGS             | 1            | 1               | 0           | 1          | 2            |
| ICONS                | 2            | 2               | 1           | 2          | 2            |
| DARK                 | 2            | 2               | 2           | 2          | 0            |
| ENDLESS-PROFILE      | 3            | 3               | 3           | 3          | 0            |
| CP-FEEDBACK          | 3            | 3               | 3           | 3          | 0            |
| SKILLS-SAVED         | 3            | 3               | 3           | 3          | 0            |
| ENGLISH-STATUS       | 1            | 1               | 1           | 1          | 0            |
| SLIDER               | 2            | 2               | 0           | 2          | 4            |
| HTTPS                | 1            | 3               | 1           | 1          | 4            |
| CUSTOM-UI            | 3            | 2               | 2           | 2          | 2            |
| FONT                 | 2            | 1               | 1           | 1          | 2            |
| SEARCH-BUTTON        | 1            | 3               | 3           | 3          | 4            |
| SAVE-CONCEPT         | 3            | 2               | 3           | 3          | 2            |
| CLICK-SKILLS         | 2            | 1               | 2           | 2          | 2            |
| SPACING              | 2            | 1               | 2           | 2          | 2            |
| OFFSETS              | 2            | 1               | 2           | 2          | 2            |
| SEARCH-LAYOUT        | 2            | 2               | 2           | 2          | 0            |
| CLICK-STUDENTS       | 2            | 1               | 1           | 1          | 2            |
| SEARCH-PASSWORD      | 1            | 2               | 3           | 3          | 4            |
| FILTER-RESET         | 3            | 2               | 3           | 3          | 2            |
| TIMELINE             | 3            | 3               | 2           | 3          | 2            |
| EXTERNAL-WEBSITES    | 3            | 2               | 2           | 2          | 2            |
| TFL-EDIT             | 3            | 3               | 3           | 3          | 0            |
| DELETE-CALENDAR      | 3            | 3               | 2           | 3          | 2            |
| ALL-TFLS             | 1            | 3               | 3           | 3          | 4            |
| NEW-SKILL-REENTRY    | 2            | 2               | 2           | 2          | 0            |
| REORDER-CALENDAR     | 3            | 2               | 0           | 1          | 6            |
| TASK-FOR-CALENDAR    | 3            | 3               | 3           | 3          | 0            |
| NO-ERROR-TFL-UPLOAD  | 3            | 3               | 3           | 3          | 0            |
| WHICH-REQUIRED       | 2            | 2               | 2           | 2          | 0            |
| OK-BUTTON            | 1            | 2               | 1           | 1          | 2            |
| SKILLS-VALIDATION    | 2            | 2               | 2           | 2          | 0            |
| DIRTY-PROFILE-LEAVE  | 3            | 3               | 3           | 3          | 0            |
| REQUIRED             | 2            | 2               | 2           | 2          | 0            |
| CANCEL-TASK-EDIT     | 3            | 3               | 3           | 3          | 0            |
| ADD-SKILL-WITH-DIRTY | 3            | 3               | 3           | 3          | 0            |
| UNCLEAR-MAIL         | 1            | 3               | 1           | 1          | 4            |
| SKILLS-UNCLEAR       | 1            | 1               | 1           | 1          | 0            |
| HOVER                | 2            | 2               | 2           | 2          | 0            |
| CONSEQUENCES         | 1            | 1               | 2           | 1          | 2            |
| FAQ                  | 1            | 1               | 1           | 1          | 0            |
| ALUMNAE              | 1            | 1               | 0           | 1          | 2            |
| TASK-TABS            | 3            | 2               | 2           | 2          | 2            |
| MISLEADING-YOUR      | 3            | 1               | 2           | 2          | 4            |
| CP-MEANING           | 1            | 1               | 1           | 1          | 0            |
| TASK-STATUS-ICON     | 2            | 1               | 2           | 2          | 2            |
| WHICH-PROFILE        | 3            | 2               | 2           | 2          | 2            |
| UNSEEN-DIRTY         | 3            | 3               | 3           | 3          | 0            |
| DASH-REDUNDANT       | 2            | 2               | 2           | 2          | 0            |
| SEARCH-FUZZY         | 1            | 3               | 3           | 3          | 4            |
| USELESS-LABELS       | 2            | 1               | 2           | 2          | 2            |
| CP-USELESS           | 3            | 1               | 3           | 3          | 4            |
| TAKS-DENSITY         | 0            | 1               | 2           | 1          | 4            |
| TFL-DESCRIPTION      | 1            | 2               | 2           | 2          | 2            |
| EMPTY-CP             | 2            | 1               | 2           | 2          | 2            |
| EMPTY-TIMELINE       | 2            | 2               | 2           | 2          | 0            |
| SKILL-FILTER         | 3            | 2               | 3           | 3          | 2            |
| USER-SHORTCUT        | 2            | 0               | 0           | 1          | 4            |
| USER-ROLE-FEEDBACK   | 2            | 1               | 2           | 2          | 2            |
| LOGGED-IN            | 1            | 1               | 2           | 1          | 2            |
| UNDO                 | 3            | 3               | 3           | 3          | 0            |
| OLD-STUDENTS         | 3            | 1               | 1           | 1          | 4            |
| NO-TFL               | 3            | 2               | 2           | 2          | 2            |
| NO-TASKS             | 3            | 3               | 3           | 3          | 0            |
| PROFILES             | 3            | 3               | 3           | 3          | 0            |
| SEMESTERS-WRONG      | 2            | 2               | 3           | 2          | 2            |
| LOCATION             | 2            | 2               | 1           | 2          | 2            |
| IMPOSSIBLE-STUDENTS  | 3            | 2               | 2           | 2          | 2            |
| EXPIRED-TASKS        | 2            | 2               | 2           | 2          | 0            |
Table: Gewichtete Problemfunde  {#tbl:heur:weighted}



### Kosmetische Probleme {#sec:heur:cosmetic}



|    Bezeichner     |     Kriterium      |                         Beschreibung                         |                         Fundorte                          |
| :---------------: | :----------------: | :----------------------------------------------------------: | :-------------------------------------------------------: |
|       DARK        |   ADAPT, CONSIST   |               Schlechte Kontraste im Darkmode.               | MANAGE, TASK.*, FAQ, STUDENT.WORK, Lade-Indikatoren,Tabs, |
|   SEARCH-LAYOUT   |      CONSIST       |      Layout von Suchergebnissen ist nicht einheitlich.       |                          SEARCH                           |
| NEW-SKILL-REENTRY |      CONTROL       | Suchergebnis wird beim erstellen eines neuen Skills nicht übernommen. |                  TASK.EDIT, STUDENT.WORK                  |
|  WHICH-REQUIRED   |     ERR-HANDLE     | Wenn benötigte Felder in der Aufgabenerstellung ausgelassen werden, so zeigt die Fehlermeldung nicht direkt, welche Felder noch gefüllt werden müssen, sondern nur, dass Eingaben fehlen. |                         TASK.EDIT                         |
| SKILLS-VALIDATION |      ERR-PREV      | Bei der Erstellung neuer Skills wird keine Validierung vorgenommen. |                       MANAGE.SKILLS                       |
|     REQUIRED      |      ERR-PREV      | Benötigte Felder in der Aufgabenerstellung werden nicht vorher gekennzeichnet. |                         TASK.EDIT                         |
|       HOVER       |        HELP        |              Es fehlen des Öfteren Hover-Texte               |             \*, bspw. TASK.* für Icon-Buttons             |
|  DASH-REDUNDANT   |       RELEV        | Dashboardbuttons führen immer zum selben, wenn man nicht eingeloggt ist. Die nicht funktionalen Buttons sind nicht notwendig. |                           DASH1                           |
|  EMPTY-TIMELINE   |       RELEV        | Leere Timeline, leere Kenntnisse etc. werden angezeigt, ohne Mehrwert zu erbringen. |                        STUDENT.UNI                        |
|   EXPIRED-TASKS   | UPTODATE, ERR-PREV | Zeitlich abgelaufene Aufgaben wurden als verfügbar angezeigt, auch wenn sie dezent als abgelaufen gekennzeichnet waren. |                          TASK.*                           |

Table: Kosmetische Probleme (einstimmig) {#tbl:cosmetical-problems}



