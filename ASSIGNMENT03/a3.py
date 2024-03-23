class ChainingTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=32):
        self.capacity = capacity
        self.table = [None] * capacity

    def insert(self, key, value):
        index = hash(key) % self.capacity
        if self.table[index] is None:
            self.table[index] = self.Record(key, value)
            return True
        current = self.table[index]
        while current.next:
            if current.key == key:
                return False  
            current = current.next
        current.next = self.Record(key, value)
        return True

    def modify(self, key, value):
        index = hash(key) % self.capacity
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return True
            current = current.next
        return False  

    def remove(self, key):
        index = hash(key) % self.capacity
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False 

    def search(self, key):
        index = hash(key) % self.capacity
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  

    def capacity(self):
        return self.capacity

    def __len__(self):
        count = 0
        for slot in self.table:
            current = slot
            while current:
                count += 1
                current = current.next
        return count
