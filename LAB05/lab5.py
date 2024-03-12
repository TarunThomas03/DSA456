from typing import Any, Optional, List

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, data: Any):
        new_node = Node(data, next_node=self.head)
        self.head = new_node

    def append(self, data: Any):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, target: Node, data: Any):
        if target is None:
            return

        new_node = Node(data, next_node=target.next)
        target.next = new_node

    def delete(self, target: Node) -> bool:
        if not self.head or target is None:
            return False

        if self.head == target:
            self.head = target.next
            return True

        current = self.head
        while current.next and current.next != target:
            current = current.next

        if current.next == target:
            current.next = target.next
            return True

        return False

    def search(self, data: Any) -> Optional[Node]:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage:
linked_list = SinglyLinkedList()
print(linked_list.is_empty())  # Output: True

linked_list.prepend(1)
linked_list.prepend(2)
linked_list.append(3)
linked_list.print()  # Output: 2 -> 1 -> 3 -> None

node_1 = linked_list.search(1)
linked_list.insert_after(node_1, 4)
linked_list.print()  # Output: 2 -> 1 -> 4 -> 3 -> None

node_2 = linked_list.search(2)
linked_list.delete(node_2)
linked_list.print()  # Output: 1 -> 4 -> 3 -> None

print(linked_list.size())  # Output: 3
print(linked_list.to_list())  # Output: [1, 4, 3]
