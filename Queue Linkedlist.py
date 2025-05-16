class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Para la cola
        self.left = None  # Para el árbol binario
        self.right = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("La cola está vacía")
            return -1
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.front is None:
            print("La cola está vacía")
            return -1
        return self.front.data

    def is_empty(self):
        return self.front is None

    def print_queue(self):
        if self.front is None:
            print("La cola está vacía")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("NULL")

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_rec(self.root, data)

    def _insert_rec(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert_rec(root.left, data)
        else:
            root.right = self._insert_rec(root.right, data)
        return root

    def inorder_traversal(self):
        self._inorder_rec(self.root)
        print()

    def _inorder_rec(self, root):
        if root:
            self._inorder_rec(root.left)
            print(root.data, end=" ")
            self._inorder_rec(root.right)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()  # 10 <- 20 <- 30 <- NULL

    print("Eliminado:", queue.dequeue())  # 10
    queue.print_queue()  # 20 <- 30 <- NULL

    print("Primer elemento:", queue.peek())  # 20

    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Recorrido Inorden:", end=" ")
    tree.inorder_traversal()  # 20 30 40 50 60 70 80
