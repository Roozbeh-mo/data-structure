class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkList:
    def __init__(self):
        self.head=None
    
    def insert_first(self,X):
        a = Node(X)
        a.next=self.head
        self.head=a
    def insert_last(self,x):
        a = Node(x)
        if not self.head:
            self.head=a
            return
        c = self.head
        while c.next :
            c=c.next
        c.next=a
    def insert_after(self,x,y):
        if not self.head :
            print("list is empty")
            return
        c = self.head
        while c:
            if c.data==x:
                a = Node(y)
                a.next=c.next
                c.next=a
                return
            c=c.next
        print("x not found")
    def insert_before(self,x,y):
        if not self.head:
            print("list is empty")
            return
        if self.head.data==x:
            self.insert_first(y)
            return
        c=self.head
        while c.next:
            if c.next.data==x:
                a = Node(y)
                a.next=c.next
                c.next=a
                return
            c=c.next
        print("x not found")
    def delete_first(self):
        if not self.head:
            print("list is empty")
            return
        if not self.head.next:
            a = self.head
            self.head=None
            del a
            return
        a = self.head
        self.head=self.head.next
        del a                            
    def delete_last(self):
        if not self.head:
            print("list is empty")
            return
        if not self.head.next:
            a = self.head
            self.head=None
            del a
            return
        c = self.head
        while c.next.next:
            c=c.next
        a=c.next
        c.next=None
        del a
    def delete_before(self, x):
        if not self.head:
            print("list is empty")
            return
        if not self.head.next:
            print("error: only one node")
            return
        if not self.head.next.next:
            if self.head.next.data == x:
                a = self.head
                self.head = self.head.next
                del a   
                return
            else:
                print("error: x not found or no node before x")
                return
        if self.head.next.data == x:
            a = self.head
            self.head = self.head.next
            del a
            return
        c = self.head
        while c.next and c.next.next:
            if c.next.next.data == x:
                a=c.next
                c.next = c.next.next
                del a
                return
            c = c.next
        print("x not found")
    def delete_after(self,x):
        if not self.head:
            print("list is empty")
            return
        if not self.head.next:
            print("error: only one node")
            return                            
        c=self.head
        while c:
            if c.data==x:
                if not c.next:
                    print("no node after x")
                    return
                a=c.next
                c.next=c.next.next
                del a
                return
            c=c.next
        print("x not found")
 
    def delete_all(self):
        while self.head:
            a = self.head
            self.head=self.head.next
            del a
        self.head = None
    #HW---------------------------------------------------
    def replace(self,old,new):
        if not self.head:
            print("list is empty")
            return
        c=self.head
        flag=False
        while c :
            if c.data==old:
                c.data=new
                flag=True
            c=c.next
        if flag:
            print("replace done")
        else:
            print("not found")
    def show(self):
        if not self.head:
            print("list is empty")
            return
        c=self.head
        while c:
            print(c.data,end="-->")
            c=c.next
        print(None)
    def search(self,x):
        if not self.head:
            print("list is empty")
            return
        c=self.head
        while c:
            if c.data==x:
                print(f"{x} exist")
                return
            c=c.next
        print("not found")
            
    def count(self):
        if not self.head:
            print("list is empty")
            return
        count=0
        c=self.head
        while c:
            count+=1
            c=c.next
        return count