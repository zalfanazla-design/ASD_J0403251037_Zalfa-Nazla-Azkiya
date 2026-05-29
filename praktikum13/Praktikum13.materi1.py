# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Materi 1 - Algoritma Kruskal
# ==========================================================

# Daftar edge:
# Format -> (bobot, node1, node2)

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge dari bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Edge dipilih jika tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)


# Kesimpulan:
# Algoritma Kruskal memilih edge dengan bobot terkecil
# terlebih dahulu tanpa membentuk cycle.
