class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return

                current = current.left

            elif value > current.value:
                if not current.right:
                    current.right = new_node
                    return

                current = current.right
            else:
                return

    def search(self, value):
        if not self.root:
            return False

        current = self.root

        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self, node=None):
        if not node:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def preorder(self, node=None):
        if not node:
            node = self.root
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node=None):
        if not node:
            node = self.root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
