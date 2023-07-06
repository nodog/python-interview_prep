

class Node:
    node_left = None
    node_right = None
    label = ""
    weight = 0

    def __init__(self, label, weight):
        self.label = label
        self.weight = weight

    def print_tree(self):
        if self.node_left:
            self.node_left.print_tree()
        self.print_node()
        if self.node_right:
            self.node_right.print_tree()

    def print_node(self):
        print(self.label, end='')

    def assemble_tree(self, tree_array):
        if self.node_left:
            self.node_left.assemble_tree(tree_array)
        tree_array.append(self)
        if self.node_right:
            self.node_right.assemble_tree(tree_array)
        return tree_array

    def insert_node(self, new_node):
        if new_node.weight < self.weight:
            if self.node_left:
                self.node_left.insert_node(new_node)
            else:
                self.node_left = new_node
        else: #new_node.weight >= self.weight:
            # insert new node right
            if self.node_right:
                self.node_right.insert_node(new_node)
            else:
                self.node_right = new_node


def rebalance_tree(tree_root):
    print("--rebalance--")
    
    tree_array = tree_root.assemble_tree([])

    new_tree_root_node = tree_array[round(len(tree_array)/2)]
    new_tree_root = Node(new_tree_root_node.label, new_tree_root_node.weight)

    for node in tree_array:
        node.print_node()
        if node is not new_tree_root_node:
            new_tree_root.insert_node(Node(node.label, node.weight))
    print()

    return new_tree_root

if __name__ == "__main__":
    print("--- rebalance a tree ---")

    tree_root = Node("G", 0)
    
    tree_root.print_tree()
    print()
    
    tree_root.insert_node(Node("A", 1))

    tree_root.print_tree()
    print()

    tree_root.insert_node(Node("A", 10))
    tree_root.insert_node(Node("O", 7))
    tree_root.insert_node(Node("Z", 8))
    tree_root.insert_node(Node("R", 2))
    tree_root.insert_node(Node("M", 3))
    tree_root.insert_node(Node("I", 9))
    tree_root.insert_node(Node("O", 4))
    tree_root.insert_node(Node("N", 5))
    tree_root.insert_node(Node("B", 6))

    tree_root.print_tree()
    print()

    tree_root.print_node()
    print()

    new_tree_root = rebalance_tree(tree_root)

    new_tree_root.print_node()
    print()
    new_tree_root.print_tree()
    print()
