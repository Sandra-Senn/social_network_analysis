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


Die vorliegende Analyse hat die Grundstruktur des Curriculums mittels Netzwerkanalyse untersucht. Zahlreiche weiterführende Ansätze wären möglich gewesen, um ein noch umfassenderes Bild zu erhalten:

**Erweiterte Visualisierungen**
Interaktive Netzwerkdarstellungen mit Plotly oder D3.js hätten eine explorative Analyse ermöglicht, bei der Nutzer Module anklicken, filtern und verschiedene Perspektiven einnehmen können. Animierte Visualisierungen des Studienverlaufs über Semester hinweg würden die zeitliche Dimension besser erfassen. Heatmaps der Modulbelegung mit flexiblen Filteroptionen nach Semestern, Themenbereichen oder Schwierigkeitsgraden hätten zusätzliche Einsichten ermöglicht.

**Temporale Analyse**
Die Integration vollständiger Semesterinformationen für alle Module hätte eine präzisere Analyse optimaler Belegungsreihenfolgen ermöglicht. Algorithmen zur Optimierung von Studienverläufen unter Berücksichtigung von Voraussetzungen und Kapazitäten wären wertvoll gewesen. Die Simulation verschiedener Studienpfade hätte gezeigt, welche Wahlentscheidungen zu längeren oder kürzeren Studienzeiten führen.

**Vergleichende Studien**
Ein systematischer Vergleich mit Curricula anderer Hochschulen hätte Stärken und Schwächen des untersuchten Studiengangs aufgezeigt. Benchmarking gegen identifizierte Best Practices in der Curriculum-Gestaltung hätte konkrete Verbesserungsvorschläge generieren können. Die Mustererkennung in erfolgreichen Curriculumstrukturen hätte allgemeine Designprinzipien offenbart.

**Integration realer Studiendaten**
Die Analyse anonymisierter Studienverläufe hätte den Abgleich zwischen geplanter und tatsächlicher Modulbelegung ermöglicht. Die empirische Identifikation praktischer Bottlenecks würde zeigen, wo die größten Herausforderungen im realen Studienbetrieb liegen. Die Analyse von Erfolgsquoten in Abhängigkeit von der Netzwerkposition einzelner Module hätte deren tatsächliche Schwierigkeit offenbart.

**Methodische Vertiefung**
Der systematische Vergleich verschiedener Community-Detection-Algorithmen (Louvain, Infomap, Leiden, Label Propagation) hätte die Robustheit der identifizierten Modulgruppen validiert. Die Analyse hierarchischer Community-Strukturen über mehrere Ebenen würde feinere thematische Untergliederungen offenbaren. Die Detektion überlappender Communities wäre besonders für interdisziplinäre Module relevant gewesen.

**Multiplex-Netzwerkanalyse**
Die Modellierung verschiedener Beziehungstypen (Voraussetzungen, Empfehlungen, zeitliche Inkompatibilitäten) in einem multiplen Netzwerk hätte die Komplexität des Curriculums besser abgebildet. Die schichtübergreifende Analyse von Interdependenzen würde zeigen, wie verschiedene Arten von Abhängigkeiten zusammenwirken. Die Identifikation kritischer Layer im Gesamtnetzwerk könnte Prioritäten für Optimierungsmaßnahmen setzen.


## Autoren

- Sandra Senn
- Michelle Rohrer

