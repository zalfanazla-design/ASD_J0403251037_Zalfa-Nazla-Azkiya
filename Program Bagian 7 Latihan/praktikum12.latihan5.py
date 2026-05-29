# Nama : Zalfa Nazla Azkiya
# NIM : J0403251037
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Node awal = 0
    distances[start] = 0

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        # Mengecek semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Node awal
start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
#
# 2. Node yang memiliki jarak paling kecil dari node awal
#    adalah Depok dengan jarak 2.
#
# 3. Node yang memiliki jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.
#
# 4. Algoritma Dijkstra bekerja dengan memilih node yang
#    memiliki jarak paling kecil terlebih dahulu, lalu
#    memperbarui jarak ke node tetangga sampai semua
#    node mendapatkan jarak minimum.