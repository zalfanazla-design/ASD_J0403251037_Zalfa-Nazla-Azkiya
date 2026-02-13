class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
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
        new_node.prev = temp


    # Method untuk mencari elemen
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# =======================================
#                   LATIHAN 3
#========================================

dll = DoublyLinkedList()

# Memasukkan data
data = [2, 6, 9, 14, 20, 50, 57, 68, 83]
for item in data:
    dll.append(item)

print("Masukkan elemen ke dalam Doubly Linked List:", data)

# Input pencarian
cari = int(input("Masukkan elemen yang ingin dicari: "))

# Cek hasil pencarian
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print("Elemen tidak ditemukan dalam Doubly Linked List.")
