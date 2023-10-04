#

class KVNode:

    def __init__(self, key, value):
        self.left_node = None
        self.right_node = None
        self.key = key
        self.value = value

    def has_child_nodes(self):
        return self.left_node != None or self.right_node != None

    def add_node(self, key, value):
        if key < self.key:
            if self.left_node == None:
                self.left_node = KVNode(key, value)
            else:
                self.left_node.add_node(key, value)
        else:
            if self.right_node == None:
                self.right_node = KVNode(key, value)
            else:
                self.right_node.add_node(key, value)

    def del_node(self, key, last_node=None):
        if key == self.key:
            if self.left_node == None and self.right_node == None:
                last_node

    def value_at(self, key, last_left_node=None):
        if key == self.key:
            return self.value
        elif key < self.key:
            if self.left_node != None:
                # print(
                # f'passing last node ({self.key}, {self.value}) moving left')
                return self.left_node.value_at(key, last_left_node)
            else:
                return last_left_node.value
        elif key > self.key:
            if self.right_node != None:
                # print(
                # f'passing last node ({self.key}, {self.value}) moving right')
                return self.right_node.value_at(key, self)
            else:
                return self.value

    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        print(self.key, self.value)
        if self.right_node:
            self.right_node.print_tree()


if __name__ == '__main__':
    root = KVNode(0, 'a')
    root.print_tree()
    print(root.has_child_nodes())
    print()
    root.add_node(4, 'b')
    root.add_node(2, 'c')
    root.add_node(6, 'd')
    root.print_tree()
    print(root.has_child_nodes())
    print(0, root.value_at(0))
    print(1, root.value_at(1))
    print(2, root.value_at(2))
    print(3, root.value_at(3))
    print(4, root.value_at(4))
    print(5, root.value_at(5))
    print(6, root.value_at(6))
    print(7, root.value_at(7))
    print(8, root.value_at(8))
