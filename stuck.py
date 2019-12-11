class stuck:
    def __init__(self):
        self.items = []
        self.default = None

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def delete(self,item):
        self.items.remove(item)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
