# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 5 - Jaringan Jalan Antar Kota
# ==========================================================

# Daftar edge
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

mst = []
total_weight = 0
connected = set()

# Algoritma Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Output hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus yang dipilih adalah jaringan jalan antar kota.
#
# 2. Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge yang dipilih:
#    Bogor-Depok
#    Depok-Jakarta
#    Depok-Bandung
#
# 4. Total bobot MST adalah 9.
#
# 5. Edge tertentu tidak dipilih karena dapat
#    membentuk cycle atau memiliki bobot lebih besar.
# ==========================================================