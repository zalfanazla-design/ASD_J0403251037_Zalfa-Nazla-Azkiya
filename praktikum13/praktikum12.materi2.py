# Nama : Zalfa Nazla Azkiya
# NIM : J040251037
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Materi 2: Implementasi Algoritma Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    # Menyimpan jarak minimum tiap node
    distances = {node: float('inf') for node in graph}

    # Node awal bernilai 0
    distances[start] = 0

    # Relaksasi edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Mengecek semua edge pada graph
        for node in graph:

            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak lebih kecil
                if distances[node] + weight < distances[neighbor]:

                    # Update jarak
                    distances[neighbor] = distances[node] + weight

    return distances

# Menjalankan algoritma dari node A
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Hasil shortest path menggunakan Bellman-Ford:")
print(hasil)

# Penjelasan:
# A -> B secara langsung memiliki bobot 5
#
# Tetapi jika melalui C:
# A -> C -> B
# = 4 + (-2)
# = 2
#
# Maka jalur melalui C lebih pendek.
#
# Bellman-Ford dapat menangani bobot negatif
# karena melakukan relaksasi edge berulang kali.