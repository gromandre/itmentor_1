class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next and current.next.value != value:
            current = current.next
        if current.next:

            current.next = current.next.next

    def find(self, value):

        if not self.head:
            return False

        current = self.head

        while current:
            if current.value == value:
                return self.head
            current = current.next

        return False