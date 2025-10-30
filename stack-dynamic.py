class Stack:
    def __init__(self,limit=10):
        self.list=[]
        self.limit=limit
    def push(self,item):
        if len(self.list)>=self.limit:
            print("Stack is full")
            return
        else:
            self.list.append(item)
            print(f"{item} added")
            return
    def pop(self):
        if not self.list:
            print("Stack is empty")
            return
        else:
            k = self.list[-1]
            self.list.pop()
            print(f"{k} deleted")
            return k
    def show(self):
        print(self.list)
            
    def find(self,item):
        if not self.list:
            print("Stack is empty")
            return
        else:
            flag = False
            for i in range(0,len(self.list)):
                if self.list[i]==item:
                    print(f"{item} is on index {i}")
                    flag = True
            if flag:
                return
            else:
                print(f"{item} doesn't exist")
                
    def replace(self,old,new):
        if not self.list:
            print("Stack is empty")
            return
        else:
            flag = False
            for i in range(0,len(self.list)):
                if self.list[i] ==old:
                    self.list[i]=new
                    flag = True
            if flag:
                print("Replace done")
            else:
                print(f"{old} doesn't exist")
    def peek(self):
        if not self.list:
            print("Stack is empty")
            return
        else:
            print(self.list[-1])
            return self.list[-1]