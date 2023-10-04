#
# implement a class that can keep track of integer ranges
#
# methods
# - add_range(label_string, begin_int, end_int)
# - check_label(int)
#

import KVNode


class RangeLibrary:
    # time saving at cost of space - implement as array
    # label_array = []
    # how to implement in another way
    # store as a set of transitional points? (i_start, 'label')
    # this feels like a good thing for a binary search tree
    # implement in another file and import!

    def __init__(self):
        self.label_array = [''] * 100
        self.label_tree = KVNode.KVNode(0, '')
        self.label_sparse = [(0, '')]
        print("--- hello from RangeLibrary instance")

    def add_range(self, label: str, i_beg: int, i_end: int) -> str:
        i = 0
        while (i < len(self.label_sparse) and self.label_sparse[i][0] <= i_beg):
            i += 1
            print(f'i = {i}')

        if i == len(self.label_sparse):
            prev_label = self.label_sparse[i - 1][1]
            self.label_sparse.append((i_beg, label))
            self.label_sparse.append((i_end + 1, prev_label))
        else:
            j = 0
            while (j < len(self.label_sparse) and self.label_sparse[i][0] <= i_end):
                j += 1
                print(f' j = {j}')

            if j == len(self.label_sparse) and self.label_sparse[j - 1][0] <= i_end:
                prev_label = self.label_sparse[j - 1][1]
                self.label_sparse = self.label_sparse[:i] + \
                    [(i_beg, label)] + [(i_end + 1, prev_label)]
            else:
                prev_label = self.label_sparse[j - 2][1]
                self.label_sparse = self.label_sparse[:i] + [
                    (i_beg, label)] + [(i_end + 1, prev_label)] + self.label_sparse[j-1:]

        print(self.label_sparse)
        return label

    def check_label(self, i: int) -> str:
        j = 0
        label = self.label_sparse[0][1]
        while (j < len(self.label_sparse) and self.label_sparse[j][0] <= i):
            label = self.label_sparse[j][1]
            j += 1

        return label

    def add_range_tree(self, label: str, i_beg: int, i_end: int) -> str:
        end_label = self.label_tree.value_at(i_end + 1)
        print(f'label = {label}, end_label = {end_label}')
        self.label_tree.add_node(i_beg, label)
        self.label_tree.add_node(i_end + 1, end_label)
        self.label_tree.remove_node_range(i_beg, i_end + 1)
        self.label_tree.print_tree()
        return label

    def check_label_tree(self, i: int) -> str:
        return self.label_tree.value_at(i)

    def add_range_array(self, label: str, i_beg: int, i_end: int) -> str:
        if i_beg <= i_end and i_beg >= 0:
            for i in range(i_beg, i_end + 1):
                self.label_array[i] = label
            return label
        else:
            return 'RangeLibrary Error'

    def check_label_array(self, i: int) -> str:
        if i < len(self.label_array) - 1:
            return self.label_array[i]
        else:
            return 'RangeLibrary Error'


if __name__ == '__main__':
    rl = RangeLibrary()
    print(f'rl.add_range("first", 1, 10) = {rl.add_range("first", 1, 10)}')
    print(f'rl.check_label(8) = {rl.check_label(8)}')
    print(f'rl.check_label(0) = {rl.check_label(0)}')
    print(f'rl.check_label(12) = {rl.check_label(12)}')
    print(f'rl.add_range("second", 10, 20) = {rl.add_range("second", 10, 20)}')
    print(f'rl.check_label(18) = {rl.check_label(18)}')
    print(f'rl.check_label(10) = {rl.check_label(10)}')
    print(f'rl.check_label(20) = {rl.check_label(20)}')
    print(f'rl.add_range("third", 8, 12) = {rl.add_range("third", 8, 12)}')
    print(f'rl.check_label(7) = {rl.check_label(7)}')
    print(f'rl.check_label(8) = {rl.check_label(8)}')
    print(f'rl.check_label(12) = {rl.check_label(12)}')
    print(f'rl.check_label(13) = {rl.check_label(13)}')
