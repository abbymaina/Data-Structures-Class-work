class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key_value):
        if key_value < self.value:
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find(self, key):
        if key < self.value:
            if self.left is None:
                return False
            return self.left.find(key)
        elif key > self.value:
            if self.right is None:
                return False
            return self.right.find(key)
        else:
            return True


if __name__ == "__main__":
    tree = TreeNode(10)
    tree.insert(5)
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(22)
    tree.insert(11)
    tree.insert(13)
    tree.insert(12)

    print("In-order traversal:")
    tree.in_order_traversal()

    print("\nPre-order traversal:")
    tree.pre_order_traversal()

    print("\nPost-order traversal:")
    tree.post_order_traversal()

    print("\nSearch results:")
    print(tree.find(22))
    print(tree.find(30))