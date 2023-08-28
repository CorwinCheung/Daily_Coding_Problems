import ctypes


def get_pointer(obj):
    return id(obj)


def dereference_pointer(address):
    return ctypes.cast(address, ctypes.py_object).value


class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0


# HONESTLY need to understand this much better and revisit it once I learn linked list stuff(in the next week)

class XORLinkedList:
    def __init__(self):
        self.nodes = [Node(None)]  # list of nodes, use index as pointer
        self.head = 1
        self.tail = 1

    def add(self, element):
        node = Node(element)
        self.nodes.append(node)
        if len(self.nodes) == 2:  # first node
            self.nodes[self.head].both = 0
        else:
            self.nodes[self.tail].both ^= len(self.nodes) - 1
            self.nodes[-1].both = self.tail
            self.tail = len(self.nodes) - 1

    def get(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        curr_idx = self.head
        prev_idx = 0
        for i in range(index):
            if curr_idx == 0:
                raise IndexError("Index out of bounds")
            next_idx = prev_idx ^ self.nodes[curr_idx].both
            prev_idx = curr_idx
            curr_idx = next_idx
        return self.nodes[curr_idx]


def main():
    xor_list = XORLinkedList()

    # add some elements to the list
    xor_list.add(1)
    xor_list.add(2)
    xor_list.add(3)
    xor_list.add(6)

    # get the element at index 1
    node = xor_list.get(1)
    print(node.value)
    print(xor_list.get(3))
    print(xor_list.get(3).value)


main()
