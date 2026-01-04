# Netzwerkanalyse von Modulvoraussetzungen im Maschinenbaustudium

## Projektbeschreibung

Dieses Projekt analysiert die Voraussetzungsstruktur von Modulen im Maschinenbaustudium mithilfe von Methoden der Social Network Analysis (SNA). Ziel ist es, kritische Module zu identifizieren, die Studienplanung zu optimieren und Erkenntnisse für die Curriculum-Entwicklung zu gewinnen.

Das Projekt umfasst:
- **Datenbeschaffung**: Automatisierte Extraktion von Modulinformationen aus PDF-Dokumenten
- **Exploratory Data Analysis**: Erste Untersuchung der Datenstruktur und -qualität
- **Netzwerkanalyse**: Umfassende Analyse der Modulvoraussetzungen mit verschiedenen SNA-Metriken

## Projektstruktur

```
social_network_analysis/
├── Meilenstein/                   # Meilenstein-Dokumente
│   └── [Ausgefüllter Meilenstein]
├── Präsentation/                  # Präsentationsmaterialien
│   └── [Aufgezeichnete Präsentation (max. 20 Min.)]
├── Source/                        # Source-Code
│   ├── notebooks/                 # Jupyter Notebooks
│   │   ├── 1_datenbeschaffung.ipynb # Webscraping und Datenextraktion
│   │   ├── 2_datenanalyse.ipynb     # Exploratory Data Analysis
│   │   └── 3_netzwerkanalyse.ipynb # Hauptanalyse (Netzwerkanalyse)
│   ├── export_graphs.py          # Script zum Export der Graphen
│   └── requirements.txt          # Python-Abhängigkeiten
├── Rohdaten/                      # Rohdaten-Ausgaben
│   ├── data.csv                  # Vollständige Moduldaten (Rohdaten)
│   ├── nodes.csv                 # Modulknoten mit Attributen
│   ├── edges.csv                 # Voraussetzungsbeziehungen
│   └── Modultabelle Maschinenbau_HS2025_updated.pdf
├── Graphen/                       # Exportierte Netzwerk-Graphen
├── doc/                           # Zusätzliche Dokumentation
│   ├── SNA-Projektbeschreibung.pdf
│   ├── Modultabelle Maschinenbau_HS2025_updated.pdf
│   ├── Bewertungsraster.xlsx
│   └── Meilenstein-SNA-Projekt-Sandra-Michelle.docx
└── README.md                     
```

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)
- Homebrew (für macOS, zur Installation von Graphviz)

### System-Abhängigkeiten

Für die Visualisierung mit Graphviz wird das System-Tool Graphviz benötigt:

**macOS:**
```bash
brew install graphviz
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install graphviz graphviz-dev
```

**Windows:**
Download von [Graphviz Website](https://graphviz.org/download/)

### Python-Umgebung einrichten

1. Repository klonen oder herunterladen:
```bash
cd social_network_analysis
```

2. Virtuelle Umgebung erstellen (empfohlen):
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# oder
.venv\Scripts\activate  # Windows
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Graphviz Python-Binding installieren:
```bash
# macOS (nach Homebrew-Installation)
pip install pygraphviz --global-option="build_ext" --global-option="-I$(brew --prefix graphviz)/include" --global-option="-L$(brew --prefix graphviz)/lib"

# Linux
pip install pygraphviz
```

## Verwendung

### Notebooks ausführen

Die Analyse erfolgt in drei aufeinander aufbauenden Notebooks:

1. **Datenbeschaffung** (`notebooks/datenbeschaffung.ipynb`)
   - Extrahiert Modulinformationen aus PDF-Dokumenten
   - Erstellt `nodes.csv` und `edges.csv`

2. **Exploratory Data Analysis** (`notebooks/eda.ipynb`)
   - Untersucht Datenqualität und -struktur
   - Bereitet Daten für die Netzwerkanalyse vor

3. **Netzwerkanalyse** (`notebooks/netzwerkanalyse.ipynb`)
   - Hauptanalyse mit umfassenden SNA-Metriken
   - Visualisierungen und Interpretationen


## Ausblick

Die vorliegende Analyse hat die Grundstruktur des Curriculums mit Netzwerkanalyse-Methoden untersucht. Folgende Punkte zeigen konkret, welche Aspekte noch angepasst oder erweitert werden können, damit die Ergebnisse praxisnäher oder ausführlicher werden:

- **Granularität:** Zeitliche Auflösung (Semester vs. Jahr), Aggregationslevel (Module vs. Themenbereiche) und Attributfeinheit (Lehrveranstaltungen, Dozierende) variieren, um verschiedene Fragestellungen zu bedienen.
- **Methoden- und Parameterwahl:** Zentralitätsmasse, Schwellen für Dichte- oder Verbindungsschnittmengen, sowie Community-Detection-Parameter (z. B. Auflösungsparameter) anpassen und vergleichen, um Robustheit zu prüfen.
- **Multiplex-Modelle:** Zusätzliche Beziehungstypen (Empfehlungen, zeitliche Inkompatibilitäten, Kapazitätsbeschränkungen) als separate Schichten modellieren und schichtübergreifende Analysen durchführen.
- **Simulationen & Optimierung:** Studienverlaufs-Simulationen mit unterschiedlichen Randbedingungen (Kapazitäten, Wahlpräferenzen) und Optimierungszielen (Studienzeit minimieren, Auslastung glätten) ermöglichen.
- **Validierung mit Real‑Daten:** Anonymisierte Studienverläufe und Leistungsdaten integrieren, um Befunde empirisch zu prüfen und Engpässe zu identifizieren.
- **Dokumentation & Reproduzierbarkeit:** Parameter, Varianten und Datenpipeline klar dokumentieren; Skripte parametrisieren, damit Anpassungen einfach getestet werden können.
- **Dozierende & Workload-Analyse:** In zukünftigen Erweiterungen sollten Dozierenden-Daten ergänzt werden (Zuordnung Dozierender → Module, Anzahl gelehrter Module, Kontaktstunden). Damit lassen sich Workload-Verteilungen analysieren, Dozierende identifizieren, die viele oder zentral vernetzte Module betreuen, und potenzielle Engpass- oder Abhängigkeitspersonen erkennen.
- **Stundenplandaten & Optimierung:** Genaue Stundenplandaten (Termine, Zeiten, Räume) integrieren, um Überschneidungen und zeitliche Konflikte zu erkennen. Auf dieser Grundlage sind automatische Konflikterkennung, Vorschläge zur Verlagerung/Konsolidierung von Veranstaltungen und Optimierungen zur Minimierung von Überschneidungen möglich.

Priorisierungsvorschlag: zuerst Vorverarbeitung (Datenqualität & Semesterinformationen), dann robuste Methodenvergleiche (Community‑ und Zentralitätsvarianten), danach interaktive Visualisierungen und optional Multiplex‑Modelle.


## Autoren

- Sandra Senn
- Michelle Rohrer

