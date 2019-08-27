class Node:
    def __init__(self,data):
          self.data=data
          self.next=None
class Stack:
    def __init__(self):
          self.head=None 
          self.size=0
    def push(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node
        self.size+=1

    def pop(self,data=None):
        if(data is None):
            if(self.head is None):
                print("the list is empty")
                return
            obj=self.head.data
            self.head=self.head.next
            self.size-=1
            return obj
        else:   
            t=self.head
            while(t!=None and t.data!=data):
                prev=t
                t=t.next
            if(t!=None):
                prev.next=t.next 
            else:
                print("the number not found")  

    def peek(self):
        return self.head.data

    def countsize(self):
        print('the size of the stack is',self.size)


    def isempty(self):
        if(self.size==0):
            return True
        else:
            return False


    def search(self,data):
        t=self.head
        count=self.size-1
        while(t):
            if(t.data==data):
                return count
                break
            t=t.next
            count-=1
            
        return -1    

    def printstack(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next
