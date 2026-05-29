# ==========================================================
# Nama  : Zalfa Nazla Azkiya
# NIM   : J0403251037
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
# Materi 2 - Algoritma Prim
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Node awal dimasukkan ke visited
    visited = set([start])

    # Menyimpan edge yang akan diproses
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Selama masih ada edge
    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan algoritma Prim
mst, total = prim(graph, 'A')

# Output hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)


# Kesimpulan:
# Algoritma Prim membangun MST mulai dari node awal
# kemudian memilih edge terkecil secara bertahap.
