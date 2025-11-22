class dNode:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, item):
        a = dNode(item)
        if not self.head:
            self.head = a
            self.size = 1
            print(f"stack is {self.size} , limit is {self.limit}")
            return a
        c = self.head
        while c.next:
            c = c.next
        c.next = a
        a.back = c
        self.size += 1
        print(f"stack is {self.size} , limit is {self.limit}")
        return a

    def delete_last(self):
        if not self.head:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size = 0
            return data
        c = self.head
        while c.next:
            c = c.next
        data = c.data
        c.back.next = None
        self.size -= 1
        return data

    def get_last(self):
        if not self.head:
            return None
        c = self.head
        while c.next:
            c = c.next
        return c.data

    def replace(self, old, new):
        c = self.head
        flag = False
        while c:
            if c.data == old:
                c.data = new
                flag = True
            c = c.next
        return flag

    def find(self, item):
        c = self.head
        idx = 0
        while c:
            if c.data == item:
                return idx
            c = c.next
            idx += 1
        return None

    def show(self):
        c = self.head
        while c:
            print(c.data, end=" --> ")
            c = c.next
        print(None)
        
class Stack():
    def __init__(self, limit=10):
        self.list = LinkedList()
        self.limit = limit
        self.list.limit = limit


    def push(self, item):
        if self.list.size >= self.limit:
            print("stack is full")
            return
        self.list.add_last(item)
        print(f"{item} added")

    def pop(self):
        data = self.list.delete_last()
        if data is None:
            print("Stack is empty")
            return None
        print(f"{data} deleted")
        return data

    def peek(self):
        data = self.list.get_last()
        if data is None:
            print("Stack is empty")
            return None
        print(f"Top element: {data}")
        return data

    def replace(self, old, new):
        if self.list.replace(old, new):
            print("Replace done")
        else:
            print(f"{old} doesn't exist")

    def find(self, item):
        pos = self.list.find(item)
        if pos is None:
            print(f"{item} doesn't exist")
        else:
            print(f"{item} is at position {pos}")

    def show(self):
        if self.list.size == 0:
            print("none")
            return
        self.list.show()
        