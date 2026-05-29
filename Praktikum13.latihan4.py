# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 4 - Studi Kasus Jaringan Kabel
# ==========================================================

# Daftar edge
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge
edges.sort()

mst = []
total_weight = 0
connected = set()

# Algoritma Kruskal
for weight, u, v in edges:

    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Output
print("Jaringan Kabel Minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge yang dipilih:
#    GedungC-GedungD
#    GedungA-GedungC
#    GedungB-GedungD
#
# 3. Total biaya minimum adalah 6.
#
# 4. Karena MST membantu mencari koneksi
#    paling efisien dengan biaya minimum.
# ==========================================================