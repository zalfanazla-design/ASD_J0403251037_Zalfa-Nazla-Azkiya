# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Single Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Menampilkan linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # 🔥 LATIHAN 5
    # Method untuk membalik linked list TANPA membuat list baru
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Simpan next sementara
            current.next = prev      # Balik arah pointer
            prev = current           # Geser prev maju
            current = next_node      # Geser current maju

        self.head = prev  # Update head ke node terakhir


# ================= PROGRAM UTAMA =================

ll = LinkedList()

# Input dari user
input_data = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")

# Ubah input menjadi list angka
data_list = input_data.split(",")

for item in data_list:
    ll.append(int(item.strip()))

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()
