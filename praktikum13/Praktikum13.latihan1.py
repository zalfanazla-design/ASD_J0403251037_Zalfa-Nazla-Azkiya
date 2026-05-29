# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Latihan 1
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================================
# Jawaban Analisis:
#
# 1. Graph awal memiliki lebih banyak edge dan bisa
#    membentuk cycle, sedangkan spanning tree hanya
#    menghubungkan semua node tanpa cycle.
#
# 2. Karena cycle membuat koneksi menjadi tidak efisien
#    dan menambah biaya yang tidak diperlukan.
#
# 3. Karena spanning tree hanya membutuhkan
#    jumlah edge = jumlah node - 1.
# ==========================================================