class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        if self.head is None or data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def is_present(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size

if __name__ == "__main__":
    sorted_list = SortedLinkedList()
    sorted_list.insert(5)
    sorted_list.insert(3)
    sorted_list.insert(7)
    sorted_list.insert(2)
    print("Length of sorted list:", len(sorted_list))
    print("Is 3 present in the list?", sorted_list.is_present(3))
    print("Is 4 present in the list?", sorted_list.is_present(4))
    sorted_list.remove(3)
    print("Length of sorted list after removing 3:", len(sorted_list))
