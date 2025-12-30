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
│   │   ├── datenbeschaffung.ipynb # Webscraping und Datenextraktion
│   │   ├── eda.ipynb             # Exploratory Data Analysis
│   │   └── netzwerkanalyse.ipynb # Hauptanalyse (Netzwerkanalyse)
│   ├── export_graphs.py          # Script zum Export der Graphen
│   └── requirements.txt          # Python-Abhängigkeiten
├── Rohdaten/                      # Rohdaten-Ausgaben
│   ├── data.csv                  # Vollständige Moduldaten (Rohdaten)
│   ├── nodes.csv                 # Modulknoten mit Attributen
│   ├── edges.csv                 # Voraussetzungsbeziehungen
│   └── Modultabelle Maschinenbau_HS2025_updated.pdf
├── Graphen/                       # Exportierte Netzwerk-Graphen
│   ├── modulnetzwerk.graphml     # NetworkX Standard-Format
│   ├── modulnetzwerk.gexf        # Gephi-kompatibel
│   ├── modulnetzwerk.json        # JSON-Format (Web-Visualisierungen)
│   ├── modulnetzwerk.gml         # Graph Modeling Language
│   ├── modulnetzwerk.net         # Pajek-Format
│   ├── modulnetzwerk.dot         # Graphviz-Format
│   ├── modulnetzwerk.pickle      # Python Pickle-Format
│   ├── edges_export.csv          # Edge-Liste mit Attributen
│   ├── nodes_export.csv          # Node-Liste mit Attributen
│   ├── adjazenzmatrix.csv        # Adjazenzmatrix-Darstellung
│   └── edgelist.txt              # Einfache Text-Edge-Liste
├── doc/                           # Zusätzliche Dokumentation
│   ├── SNA-Projektbeschreibung.pdf
│   ├── Modultabelle Maschinenbau_HS2025_updated.pdf
│   ├── Bewertungsraster.xlsx
│   └── Meilenstein-SNA-Projekt-Sandra-Michelle.docx
└── README.md                      # Diese Datei
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

### Kurzfristige Erweiterungen

1. **Erweiterte Visualisierungen**
   - Interaktive Netzwerkvisualisierungen mit Plotly oder D3.js
   - Animierte Darstellung des Studienverlaufs
   - Semester-basierte Heatmaps der Modulbelegung

2. **Temporale Analyse vertiefen**
   - Vollständige Semester-Informationen für alle Module
   - Analyse optimaler Belegungsreihenfolgen
   - Simulation verschiedener Studienverläufe

3. **Robustheitsanalyse erweitern**
   - Simulation von Modulausfällen
   - Identifikation alternativer Studienpfade
   - Empfehlungssystem für flexible Studienplanung

### Mittelfristige Entwicklungen

1. **Vergleichende Analyse**
   - Vergleich mit anderen Studiengängen
   - Benchmarking gegen Best Practices
   - Identifikation von Mustern in erfolgreichen Curricula

2. **Prädiktive Modellierung**
   - Vorhersage von Studienverzögerungen basierend auf Modulstruktur
   - Identifikation von Risikofaktoren für Studienabbrüche
   - Empfehlungssystem für individuelle Studienplanung

3. **Integration von Studentendaten**
   - Analyse tatsächlicher Studienverläufe
   - Vergleich geplanter vs. tatsächlicher Belegungen
   - Identifikation von Bottlenecks in der Praxis

### Langfristige Vision

1. **Dynamische Curriculum-Optimierung**
   - Automatische Vorschläge für Curriculum-Verbesserungen
   - Simulation von Änderungen vor Implementierung
   - Kontinuierliche Anpassung basierend auf Studienerfolg

2. **Interaktive Planungstools**
   - Web-basiertes Tool für Studienplanung
   - Personalisierte Empfehlungen für Studenten
   - Integration in bestehende Studienverwaltungssysteme

3. **Multi-Level-Analyse**
   - Analyse auf verschiedenen Ebenen (Module, Kurse, Lerneinheiten)
   - Integration von Lernzielen und Kompetenzen
   - Verbindung mit Learning Analytics

4. **Erweiterte Netzwerkanalyse**
   - Gewichtete Netzwerke (z.B. basierend auf Schwierigkeit)
   - Multipartite Netzwerke (Module, Dozenten, Räume, Zeiten)
   - Dynamische Netzwerke (Änderungen über Zeit)

5. **Machine Learning Integration**
   - Clustering von ähnlichen Modulen
   - Empfehlungssysteme für Wahlmodule
   - Anomalieerkennung in Studienverläufen

### Methodische Erweiterungen

1. **Erweiterte Community Detection**
   - Vergleich verschiedener Algorithmen (Infomap, Leiden)
   - Hierarchische Community-Strukturen
   - Overlapping Communities

2. **Zeitliche Netzwerkanalyse**
   - Analyse von Curriculum-Änderungen über Zeit
   - Evolutionäre Netzwerkanalyse
   - Trend-Erkennung in Studienstrukturen

3. **Multiplex-Netzwerke**
   - Verschiedene Beziehungstypen (Voraussetzungen, Empfehlungen, Inkompatibilitäten)
   - Analyse von Interdependenzen zwischen verschiedenen Netzwerkebenen

### Anwendungsbereiche

1. **Studienberatung**
   - Automatisierte Studienplanungsempfehlungen
   - Früherkennung von Problemen
   - Personalisierte Beratung basierend auf Netzwerkanalyse

2. **Curriculum-Design**
   - Evidenz-basierte Curriculum-Entwicklung
   - Optimierung von Modulstrukturen
   - Evaluation von Curriculum-Änderungen

3. **Ressourcenplanung**
   - Optimale Allokation von Lehrressourcen
   - Kapazitätsplanung basierend auf kritischen Modulen
   - Prüfungsplanung unter Berücksichtigung von Abhängigkeiten

4. **Qualitätssicherung**
   - Monitoring von Studienverläufen
   - Identifikation von Problemen im Curriculum
   - Kontinuierliche Verbesserung basierend auf Daten


## Autoren

- Sandra Senn
- Michelle Rohrer

