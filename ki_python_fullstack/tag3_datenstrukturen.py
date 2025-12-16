#!/usr/bin/env python3
"""
Tag 3 — Datenstrukturen in Python
"""

# ============================================================================
# Listen (Lists)
# ============================================================================

# Listen sind geordnete, veränderbare Sammlungen von Elementen.
# Sie können Elemente hinzufügen, entfernen und ändern.
# Beispiel:

patients = ["Anna", "Max", "Lena"]

print(patients)
print(patients[0])      # erstes Element
print(len(patients))   # Anzahl der Elemente
patients.append("Tom")  # neues Element hinzufügen
print(patients)
patients.remove("Max") # Element entfernen
print(patients)
patients[1] = "Sophie" # Element ändern
print(patients)

