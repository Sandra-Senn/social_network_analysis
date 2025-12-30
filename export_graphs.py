"""
Export-Script für Netzwerk-Graphen in verschiedenen Formaten

Dieses Script exportiert das ModulNetzwerk in verschiedene
Formate für die Verwendung in verschiedenen Tools:
- GraphML: NetworkX Standard-Format
- GEXF: Gephi-kompatibel
- JSON: Für Web-Visualisierungen
- CSV: Edge-List und Node-List
- Pajek: .net Format
- Graphviz: .dot Format
"""

import networkx as nx
import pandas as pd
import json
import os
import pickle

# Erstelle Graphen-Ordner falls nicht vorhanden
os.makedirs('Graphen', exist_ok=True)

# Daten laden
print("Lade Daten...")
edges = pd.read_csv('data/edges.csv')
nodes = pd.read_csv('data/nodes.csv')

# Netzwerk aufbauen
print("Erstelle Netzwerk...")
G = nx.from_pandas_edgelist(edges, 'Source', 'Target', 
                           edge_attr='Label', create_using=nx.DiGraph())

# Knotenattribute hinzufügen
nx.set_node_attributes(G, nodes.set_index('Id')['Gruppe'].to_dict(), 'Gruppe')
nx.set_node_attributes(G, nodes.set_index('Id')['Semester'].to_dict(), 'Semester')
nx.set_node_attributes(G, nodes.set_index('Id')['Name'].to_dict(), 'Name')

print(f"Netzwerk: {G.number_of_nodes()} Knoten, {G.number_of_edges()} Kanten\n")

# 1. GraphML Format (NetworkX Standard, kompatibel mit vielen Tools)
print("Exportiere GraphML...")
nx.write_graphml(G, 'Graphen/modulnetzwerk.graphml')
print("  ✓ modulnetzwerk.graphml")

# 2. GEXF Format (Gephi-kompatibel)
print("Exportiere GEXF (für Gephi)...")
nx.write_gexf(G, 'Graphen/modulnetzwerk.gexf')
print("  ✓ modulnetzwerk.gexf")

# 3. JSON Format (für Web-Visualisierungen)
print("Exportiere JSON...")
# NetworkX JSON Format
graph_data = nx.node_link_data(G, edges="links")
with open('Graphen/modulnetzwerk.json', 'w', encoding='utf-8') as f:
    json.dump(graph_data, f, indent=2, ensure_ascii=False)
print("  ✓ modulnetzwerk.json")

# 4. CSV Formate (Edge-List und Node-List)
print("Exportiere CSV...")
# Edge-List mit Attributen
edge_list = []
for u, v, data in G.edges(data=True):
    edge_list.append({
        'Source': u,
        'Target': v,
        'Type': 'Directed',
        'Label': data.get('Label', 'Voraussetzung')
    })
pd.DataFrame(edge_list).to_csv('Graphen/edges_export.csv', index=False)

# Node-List mit Attributen
node_list = []
for node, data in G.nodes(data=True):
    node_list.append({
        'Id': node,
        'Label': node,
        'Name': data.get('Name', ''),
        'Gruppe': data.get('Gruppe', ''),
        'Semester': data.get('Semester', '')
    })
pd.DataFrame(node_list).to_csv('Graphen/nodes_export.csv', index=False)
print("  ✓ edges_export.csv")
print("  ✓ nodes_export.csv")

# 5. Pajek Format (.net)
print("Exportiere Pajek...")
nx.write_pajek(G, 'Graphen/modulnetzwerk.net')
print("  ✓ modulnetzwerk.net")

# 6. Graphviz Format (.dot) - benötigt pygraphviz
print("Exportiere Graphviz DOT...")
try:
    A = nx.nx_agraph.to_agraph(G)
    A.write('Graphen/modulnetzwerk.dot')
    print("  ✓ modulnetzwerk.dot")
except (ImportError, AttributeError):
    print("  ⚠ Graphviz DOT Export übersprungen (pygraphviz nicht verfügbar)")

# 7. Adjazenzmatrix als CSV
print("Exportiere Adjazenzmatrix...")
adj_matrix = nx.to_pandas_adjacency(G, nodelist=sorted(G.nodes()))
adj_matrix.to_csv('Graphen/adjazenzmatrix.csv')
print("  ✓ adjazenzmatrix.csv")

# 8. Edge-List (einfach, ohne Attribute)
print("Exportiere einfache Edge-List...")
nx.write_edgelist(G, 'Graphen/edgelist.txt', data=False)
print("  ✓ edgelist.txt")

# 9. GML Format (Graph Modeling Language)
print("Exportiere GML...")
nx.write_gml(G, 'Graphen/modulnetzwerk.gml')
print("  ✓ modulnetzwerk.gml")

# 10. Pickle Format (Python-spezifisch, für schnelles Laden)
print("Exportiere Pickle...")
with open('Graphen/modulnetzwerk.pickle', 'wb') as f:
    pickle.dump(G, f)
print("  ✓ modulnetzwerk.pickle")


