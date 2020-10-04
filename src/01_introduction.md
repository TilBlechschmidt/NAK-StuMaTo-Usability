---
    header-title: Usability-Analyse StuMaTo
    title: Usability-Analyse nach dem Scenario-based Development der Studentenverwaltungsplattform StuMaTo

    author: Til Blechschmidt, Hendrik Reiter, Hans Rißer 
    Zenturie: A17
    Studiengang: Angewandte Informatik
    Matrikelnummer: 8240, 8077, 8075 

    keywords: [usablity engineering, student management, heuristics, user experience lab, nordakademie, nak, ppi]
    
    # This can be replaced with any valid bibliography file (.yaml, .json, .bib)
    bibliography: src/bibliography.json

    lof: true
    lot: true
---
\renewcommand{\arraystretch}{1.5}

# Einleitung

## Projektvorstellung

Die PPI AG ist ein mittelständisches Unternehmen im Bereich Softwareconsulting für Banken und Versicherungen mit etwa 600 Mitarbeitern. Dabei bildet die PPI AG schon langjährig Duale Studenten an der Nordakademie aus. Angefangen mit Studenten der Wirtschaftsinformatik werden mittlerweile auch Studenten in den Studiengängen Betriebswirtschaftslehre und Angewandte Informatik ausgebildet. Zudem wurde auch das Portfolio an Hochschulen ausgeweitet. So bildet die PPI AG nicht nur Studenten an der Nordakademie, sondern auch an der Wirtschaftsakademie Schleswig-Holstein, Hamburg School of Business Administration und an der Technischen Hochschule Mittelhessen aus.

Um das Studium der Studenten besser managen zu können wurde StuMaTo ins Leben gerufen. StuMaTo steht dabei für Student Management Tool. Dabei ist StuMaTo als Webseite umgesetzt, die sich nur aus dem internen Netzwerk der PPI AG erreichbar ist. Es wurde von den Studenten selber entwickelt.

Im Jahr 2018 wurde eine Gruppe von drei aktiven Studenten mit der Neuentwicklung von StuMaTo beauftragt, um StuMaTo sowohl technisch auf den neusten Stand zu bringen als auch nutzerfreundlicher werden zu lassen. Diese zweite Version von StuMaTo soll in dieser Arbeit anhand des Scenario-based Development auf ihre Usability hin analysiert werden.

## Vorgehen nach dem Scenario-based Development

Das Vorgehen des Scenario-based Development wird in [@sbd] dargestellt und ist in [Abbildung @fig:sbd] nachverfolgbar.

In dieser Arbeit erfolgt dementsprechend zunächst eine Analyse des vorgestellten Projekts. Diese ist aufgeteilt in die Kontextanalyse in [Abschnitt @sec:context], eine heuristische Evaluation als Expertenverfahren in [Abschnitt @sec:heur-anal] und einen Labortest unter Einbeziehung potentieller Nutzer in [Abschnitt @sec:lab]. Diese ermöglichen die Erstellung von Problemszenarios, auf welche sich in der Designphase konzentriert wird. Dieses Szenario repräsentiert die aktuelle Situation, geht dabei aber verstärkt auf negative Eigenschaften dieser ein. Es begründet sich in den Erkenntnissen der zuvor beschriebenen Analysephasen. Die Einschränkung der weiteren Analyse auf die vorgestellten Problemszenario liegt im Rahmen der Arbeit begründet.

In der Designphase erfolgt zunächst das Aktivitätsdesign, indem die Prozesse, welche sich als problematisch erwiesen haben, neu geordnet werden. Dazu wird ein Aktivitätsszenario erstellt, in der ein optimierter Ablauf des gleichen Prozesses beschrieben wird. Mithilfe der Meinungen und Wünsche der Nutzer, die in der Analysephase aufgedeckt wurden, kann dieser Entwurf im Vorhinein bereits teils verifiziert werden.
Auf dieser Grundlage erfolgt daraufhin eine erste Ausgestaltung der Prozessunterstützung in der Anwendung durch das Informationsdesign. Mithilfe wahrnehmungspsychologischer Grundlagen wird dabei die Darstellung an die Nutzer angepasst.

Ein Interaktionsdesign findet nicht statt und Prototypen werden lediglich für die Darstellung des Informationsdesigns angefertigt. Eine iterative Bearbeitung der Designphase und der Bewertung dieser Prototypen mit den Nutzern wird nicht vorgenommen.

![Scenario-based Development aus [@sbd]](src/images/image-20201001175014886.png){#fig:sbd}
