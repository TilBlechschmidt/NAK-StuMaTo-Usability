## Anwendungsreferenz {#sec:appendix:screens}

### Sichten und Dialoge der Anwendung

| Bezeichner                      | Beschreibung                             | Übergang zu anderen Bildschirmen |
| ------------------------------- | ---------------------------------------- | -------------------------------- |
| DASH1                           | Dashboard, nicht eingeloggt              | LOGIN                            |
| DASH2                           | Dashboard, eingeloggt                    | TASK,STUDENT                     |
| LOGIN                           | Login                                    | DASH2                            |
| TASK.SINGLE                     | Aufgabenseite, Tab Einzelaufgaben        | TASK.*                           |
| TASK.PERM                       | Aufgabenseite, Tab Daueraufgaben         | TASK.*                           |
| TASK.YOUR                       | Aufgabenseite, Tab Deine Aufgaben        | TASK.*                           |
| TASK.ALL                        | Aufgabenseite, Tab Alle Aufgaben         | TASK.*                           |
| TASK.NEW                        | Dialog zum Erstellen einer neuen Aufgabe | TASK.EDIT                        |
| TASK.VIEW                       | Ansichtsdialog einer Aufgabe             | TASK.EDIT                        |
| TASK.EDIT                       | Editierdialog einer Aufgabe              | TASK.SINGLE |
| STUDENT.LIST                    | Auflistung aller Studenten |STUDENT.UNI|
| STUDENT.UNI                     | Studentenprofil, Tab Uni |STUDENT.WORK, STUDENT.UNI.*|
| STUDENT.UNI.EDIT-STUDY          | Dialog zur Bearbeitung des eigenen Studienganges bzw. -fortschritts |STUDENT.UNI|
| STUDENT.UNI.NEW-TFL             | Dialog zur Anlage einer neuen Transferleistung |STUDENT.UNI|
| STUDENT.WORK                  | Studentenprofil, Tab Praxis |STUDENT.WORK.*|
| STUDENT.WORK.NEW-ENTRY  | Dialog zur Anlage eines neuen Kalendereintrages. |STUDENT.WORK|
| STUDENT.WORK.EDIT-ENTRY | Dialog zur Bearbeitung eines Kalendereintrages. |STUDENT.WORK|
| MANAGE.USER                     | Verwaltungsbereich für die Nutzerverwaltung. |MANAGE.*|
| MANAGE.SKILLS                   | Verwaltungsbereich für die Kenntnisverwaltung. |MANAGE.*|
| MANAGE.UNI                      | Verwaltungsbereich für die Hochschulverwaltung. |MANAGE.*|
| MANAGE.STUDENTS                 | Verwaltungsbereich für die Studentenverwaltung. |MANAGE.*|
| FAQ                             | FAQ. |-|
| SEARCH                          | Suchfunktion |-|
Table: Übersicht über Sichten der Anwendung {#tbl:screens}

Über die Navigation ist in eingeloggtem Zustand stets der Übergang zu DASH2,TASK.LIST,STUDENT.UNI, SEARCH und FAQ verfügbar. Bei einem Login als Administrator außerdem der Übergang zu MANAGE, bei einem Login als nicht Administrator auf die STUDENT.UNI Ansicht des eigenen Profils. 

### Bildschirmabzüge

Im folgenden sind zu den vorab katalogisierten Sichten Bildschirmabzüge zu finden. Diese sind aus Darstellungsgründen skaliert, damit alle Bildschirminhalte auf ein Bild passen. Dadurch sind sie *nicht* gleichwertig mit einer Nutzersicht. Die Navigationsleiste ist einheitlich und kann als intuitive Referenz für das Ausmaß dieser Skalierung dienen.

![Ansicht DASH1](src/images/image-20200919102126860.png)

![Ansicht DASH2](src/images/image-20200919104714102.png)

![Ansicht LOGIN](src/images/image-20200919102145165.png)

![Ansicht TASK.SINGLE](src/images/image-20200919102236359.png)

![Ansicht TASK.PERM](src/images/image-20200919102310902.png)

![Ansicht TASK.YOUR](src/images/image-20200919102331609.png)

![Ansicht TASK.ALL](src/images/image-20200919102343633.png)

![Ansicht TASK.NEW](src/images/image-20200919110853828.png)

![Ansicht TASK.VIEW](src/images/image-20200919102407668.png)

![Ansicht TASK.EDIT](src/images/image-20200919102504325.png)

![Ansicht STUDENT.LIST](src/images/image-20200919102606910.png)

![Ansicht STUDENT.UNI](src/images/image-20200919104135028.png)

![Ansicht STUDENT.UNI.EDIT-STUDY](src/images/image-20200919104218732.png)

![Ansicht STUDENT.UNI.NEW-TFL](src/images/image-20200919104312203.png)

![Ansicht STUDENT.WORK](src/images/image-20200919102754211.png)

![Ansicht STUDENT.WORK.NEW-ENTRY](src/images/image-20200919102823202.png)

![Ansicht STUDENT.WORK.EDIT-ENTRY](src/images/image-20200919104415404.png)

![Ansicht MANAGE.USER](src/images/image-20200919103132170.png)

![Ansicht MANAGE.SKILLS](src/images/image-20200919103418729.png)

![Ansicht MANAGE.UNI](src/images/image-20200919103450442.png)

![Ansicht MANAGE.STUDENTS](src/images/image-20200919103515258.png)

![Ansicht FAQ](src/images/image-20200919103804907.png)

![Ansicht SEARCH](src/images/image-20200919103915084.png)
