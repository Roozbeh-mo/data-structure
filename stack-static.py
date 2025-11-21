class Stack:
    def __init__(self, limit=10):
        self.list = [None] * limit   
        self.limit = limit
        self.top = -1              

    def push(self, item):
        if self.top >= self.limit - 1:
            print("Stack is full")
            return
        else:
            self.top += 1
            self.list[self.top] = item
            print(f"{item} added")
            return

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            k = self.list[self.top]
            self.list[self.top] = None
            self.top -= 1
            print(f"{k} deleted")
            return k

    def show(self):
        print(self.list[:self.top + 1])

    def find(self, item):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            flag = False
            for i in range(self.top + 1):  
                if self.list[i] == item:
                    print(f"{item} is on index {i}")
                    flag = True
            if not flag:
                print(f"{item} doesn't exist")

    def replace(self, old, new):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            flag = False
            for i in range(self.top + 1):
                if self.list[i] == old:
                    self.list[i] = new
                    flag = True
            if flag:
                print("Replace done")
            else:
                print(f"{old} doesn't exist")

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        else:
            print(self.list[self.top])
            return self.list[self.top]