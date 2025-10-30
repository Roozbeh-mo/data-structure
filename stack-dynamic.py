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
    def show(self):
        print(self.list)
            
    def find(self,item):
        if not self.list:
            print("Stack is empty")
            return
        else:
            for i in range(0,len(self.list)):
                if self.list[i]==item:
                    print(f"{item} is on {i} index")
                    return
                else:
                    print(f"{item} doesn't exist")
                    return
                
    def replace(self,old,new):
        if not self.list:
            print("Stack is empty")
            return
        else:
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
            return 
c =Stack(5)
c.push(1)
c.push(2)
c.push(3)
c.push(4)
c.push(5)
c.push(6)
c.push(7)
c.show()
c.pop()
c.show()
c.peek()
c.replace(4,999)
c.show()




