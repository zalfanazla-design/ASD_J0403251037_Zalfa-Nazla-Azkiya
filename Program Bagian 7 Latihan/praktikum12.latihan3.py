# Nama : Zalfa Nazla Azkiya
# NIM : J0403251037
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Node awal bernilai 0
    distances[start] = 0

    # Relaksasi edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
#
# 2. Total bobot jalur A -> C -> B adalah 2.
#    Karena 4 + (-2) = 2.
#
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B
#    adalah jalur melalui C.
#
# 4. Bellman-Ford dapat digunakan pada graph berbobot negatif
#    karena algoritma ini melakukan relaksasi semua edge
#    secara berulang sehingga tetap bisa menemukan
#    jarak minimum dengan benar.
#
# 5. Relaksasi edge adalah proses memperbarui jarak node
#    jika ditemukan jalur yang lebih pendek.
#
# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah:
#    Dijkstra lebih cepat tetapi tidak bisa menangani
#    bobot negatif, sedangkan Bellman-Ford bisa
#    menangani bobot negatif tetapi prosesnya lebih lambat.