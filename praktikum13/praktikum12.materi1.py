# Nama : Zalfa Nazla Azkiya
# NIM : J0403251037
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Materi 1: Implementasi Algoritma Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):

    # Menyimpan jarak minimum setiap node
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue digunakan untuk mengambil node
    # dengan jarak terkecil
    pq = [(0, start)]

    while pq:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Mengecek semua tetangga node
        for neighbor, weight in graph[current_node].items():

            # Menghitung total jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Menjalankan algoritma dari node A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Hasil shortest path menggunakan Dijkstra:")
print(hasil)

# Penjelasan:
# A ke A = 0
# A ke B = 4
# A ke C = 2
# A ke D = 3
#
# Jalur tercepat menuju D adalah:
# A -> C -> D
# dengan total bobot 2 + 1 = 3