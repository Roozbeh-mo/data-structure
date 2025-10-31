class Queue:
    def __init__(self,limit=10):
        self.list=[]
        self.front=-1
        self.rear=-1
        self.limit=limit
    def is_full(self):
        if len(self.list)>=self.limit:
            return True
        else:
            return False
    def is_empty(self):
        if self.front == -1 :
            return True
        else:
            return False
    def one_item(self):
        if self.rear==0:
            return True
        else:
            return False
        
        
    def add(self,item):
        if self.is_full():
            print("queue is full")
            return
        if self.is_empty():
            self.front=0
            self.rear=0
            self.list[self.rear]=item
            print(f"{item} added")
            return
        self.rear+=1
        self.list[self.rear]=item
        print(f"{item} added")
    
    def remo(self):
        if self.is_empty():
            print("queue is empty")
            return
        if self.one_item():
            self.front=-1
            self.rear=-1
            return
        self.front+=1
    def show_valid(self):
        if self.is_empty():
            print("queue is empty")
            return
        print(self.list[self.front:self.rear+1])
    def replace(self,old,new):
        if self.is_empty():
            print("queue is empty")
            return
        flag=False
        for i in range(self.front,self.rear+1):
            if self.list[i]==old:
                self.list[i]=new
                flag=True
        if flag:
            print("replace done")
        else:
            print(f"{old} doesn't exist")
    def shift(self):
        if self.is_empty():
            print("queue is empty")
            return
        if self.front=0
        count=self.rear - self.front+1
        for i in range(count):
            self.list[i]=self.list[self.front+i]
        self.list = self.list[:count]
        self.front=0
        self.rear=count-1

                
        
            
