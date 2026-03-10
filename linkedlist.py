# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)
        if not self.head:
            self.head = node_baru
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = node_baru

    def tampil(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.tambah(10)
ll.tambah(20)
ll.tambah(30)

ll.tampil()