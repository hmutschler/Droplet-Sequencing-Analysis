#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Parameter
total_runs = 1000000
sequence_length = 30
p_1 = 0.25  # Wahrscheinlichkeit für 1
p_0 = 1 - p_1

# Speicher
serien_k1 = []
serien_k2 = []

# Zähler
count_k1 = 0
count_k2 = 0
count_kombiniert = 0

# Hilfsfunktion: längste Serie von Einsen irgendwo
def max_series_length(arr):
    max_len = curr_len = 0
    for val in arr:
        if val == 1:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len

# Hilfsfunktion: prüft Kriterium 1 (≥7 Einsen, startet bei 0/1/2 oder endet bei 27/28/29)
def erfüllt_kriterium_1(seq):
    # Durchsuche Sequenz nach Serien von Einsen mit Länge ≥ 7
    i = 0
    while i < len(seq):
        if seq[i] == 1:
            start = i
            while i < len(seq) and seq[i] == 1:
                i += 1
            end = i - 1
            laenge = end - start + 1
            if laenge >= 7 and (start in [0, 1] or end in [ 28, 29]):
                return True, laenge
        else:
            i += 1
    return False, 0

# Simulation
for _ in range(total_runs):
    seq = np.random.choice([0, 1], size=sequence_length, p=[p_0, p_1])

    # Kriterium 1
    k1_erfüllt, serie_len_k1 = erfüllt_kriterium_1(seq)
    if k1_erfüllt:
        serien_k1.append(serie_len_k1)
        count_k1 += 1

    # Kriterium 2
    max_len = max_series_length(seq)
    k2_erfüllt = max_len >= 20
    if k2_erfüllt:
        serien_k2.append(max_len)
        count_k2 += 1

    # Kombiniert
    if k1_erfüllt or k2_erfüllt:
        count_kombiniert += 1

# Wahrscheinlichkeiten
p_k1 = count_k1 / total_runs
p_k2 = count_k2 / total_runs
p_combined = count_kombiniert / total_runs

# Ausgabe
print(f"Wahrscheinlichkeit Kriterium 1 (≥7 Einsen an Randstellen 0–2 oder 27–29): {p_k1:.4f}")
print(f"Wahrscheinlichkeit Kriterium 2 (≥10 Einsen irgendwo):                    {p_k2:.4f}")
print(f"Kombinierte Wahrscheinlichkeit (mind. eins erfüllt):                    {p_combined:.4f}")

# Histogramm (optional)
bin_range = range(7, 31)
hist_k1, _ = np.histogram(serien_k1, bins=bin_range)
hist_k2, _ = np.histogram(serien_k2, bins=bin_range)

hist_k1_percent = (hist_k1 / total_runs) * 100
hist_k2_percent = (hist_k2 / total_runs) * 100
bin_centers = np.array(bin_range[:-1]) + 0.5
bar_width = 0.4

plt.figure(figsize=(10, 6))
plt.bar(bin_centers, hist_k1_percent, width=bar_width, label="Kriterium 1 (Rand, ≥7)", color='royalblue', alpha=0.6)
plt.bar(bin_centers + bar_width, hist_k2_percent, width=bar_width, label="Kriterium 2 (Überall, ≥10)", color='seagreen', alpha=0.6)

plt.xlabel("Serienlänge")
plt.ylabel("Häufigkeit in % (von 100000 Sequenzen)")
plt.title("Histogramm der Serienlängen (p=0.76 für 1)")
plt.xticks(bin_centers + bar_width / 2, labels=range(7, 30))
plt.ylim(0, max(max(hist_k1_percent), max(hist_k2_percent)) + 1)
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Parameter
total_runs = 1000000
sequence_length = 30
p_1 = 0.76  # Wahrscheinlichkeit für 1
p_0 = 1 - p_1

# Speicher
serien_k1 = []
serien_k2 = []

# Zähler
count_k1 = 0
count_k2 = 0
count_kombiniert = 0

# Hilfsfunktion: längste Serie von Einsen irgendwo
def max_series_length(arr):
    max_len = curr_len = 0
    for val in arr:
        if val == 1:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len

# Hilfsfunktion: prüft Kriterium 1 (≥7 Einsen, startet bei 0/1 oder endet bei 28/29)
def erfüllt_kriterium_1(seq):
    # Durchsuche Sequenz nach Serien von Einsen mit Länge ≥ 7
    i = 0
    while i < len(seq):
        if seq[i] == 1:
            start = i
            while i < len(seq) and seq[i] == 1:
                i += 1
            end = i - 1
            laenge = end - start + 1
            if laenge >= 7 and (start in [0, 1 ] or end in [ 28, 29]):
                return True, laenge
        else:
            i += 1
    return False, 0

# Simulation
for _ in range(total_runs):
    seq = np.random.choice([0, 1], size=sequence_length, p=[p_0, p_1])

    # Kriterium 1
    k1_erfüllt, serie_len_k1 = erfüllt_kriterium_1(seq)
    if k1_erfüllt:
        serien_k1.append(serie_len_k1)
        count_k1 += 1

    # Kriterium 2
    max_len = max_series_length(seq)
    k2_erfüllt = max_len >= 20
    if k2_erfüllt:
        serien_k2.append(max_len)
        count_k2 += 1

    # Kombiniert
    if k1_erfüllt or k2_erfüllt:
        count_kombiniert += 1

# Wahrscheinlichkeiten
p_k1 = count_k1 / total_runs
p_k2 = count_k2 / total_runs
p_combined = count_kombiniert / total_runs

# Ausgabe
print(f"Wahrscheinlichkeit Kriterium 1 (≥7 Einsen an Randstellen 0–1 oder 28–29): {p_k1:.4f}")
print(f"Wahrscheinlichkeit Kriterium 2 (≥20 Einsen irgendwo):                    {p_k2:.4f}")
print(f"Kombinierte Wahrscheinlichkeit (mind. eins erfüllt):                    {p_combined:.4f}")

# Histogramm (optional)
bin_range = range(7, 31)
hist_k1, _ = np.histogram(serien_k1, bins=bin_range)
hist_k2, _ = np.histogram(serien_k2, bins=bin_range)

hist_k1_percent = (hist_k1 / total_runs) * 100
hist_k2_percent = (hist_k2 / total_runs) * 100
bin_centers = np.array(bin_range[:-1]) + 0.5
bar_width = 0.4

plt.figure(figsize=(10, 6))
plt.bar(bin_centers, hist_k1_percent, width=bar_width, label="Kriterium 1 (Rand, ≥7)", color='royalblue', alpha=0.6)
plt.bar(bin_centers + bar_width, hist_k2_percent, width=bar_width, label="Kriterium 2 (Überall, ≥20)", color='seagreen', alpha=0.6)

plt.xlabel("Serienlänge")
plt.ylabel("Häufigkeit in % (von 100000 Sequenzen)")
plt.title("Histogramm der Serienlängen (p=0.76 für 1)")
plt.xticks(bin_centers + bar_width / 2, labels=range(7, 30))
plt.ylim(0, max(max(hist_k1_percent), max(hist_k2_percent)) + 1)
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()

