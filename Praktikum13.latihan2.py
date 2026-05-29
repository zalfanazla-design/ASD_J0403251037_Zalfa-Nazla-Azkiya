# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 2 - Algoritma Kruskal
# ==========================================================

# Daftar edge
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

# Proses Kruskal
for weight, u, v in edges:

    # Edge dipilih jika tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Output hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Edge pertama yang dipilih adalah C-D
#    karena memiliki bobot terkecil yaitu 1.
#
# 2. Karena algoritma Kruskal bekerja dengan
#    memilih edge terkecil agar total biaya minimum.
#
# 3. Total bobot MST adalah 6.
#
# 4. Karena edge tersebut dapat membentuk cycle
#    atau memiliki bobot lebih besar.
# ==========================================================