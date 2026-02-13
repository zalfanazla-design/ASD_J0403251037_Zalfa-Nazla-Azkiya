class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Tambah node di akhir
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

    # Menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Menghapus node berdasarkan nilai
    def delete_node(self, key):
        temp = self.head

        if temp is None:
            print("List kosong")
            return

        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"Node {key} berhasil dihapus")
            return

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Node tidak ditemukan")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

        print(f"Node {key} berhasil dihapus")


# 🔥 Contoh penggunaan
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Data awal:")
dll.display()

dll.delete_node(30)

print("Setelah dihapus:")
dll.display()
