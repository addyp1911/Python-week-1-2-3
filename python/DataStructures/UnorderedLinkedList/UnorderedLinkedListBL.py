class Node:
    def __init__(self,data):
          self.data = data
          self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addfirst(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def addlast(self,data):
        new_node=Node(data)
        if(self.head is None):
            new_node=self.head
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node

    def remove(self,new_data):
        t=self.head
        prev=None
        if(self.head is None):
            print("the list is empty")
            return
        if(t!=None and t.data==new_data):
                self.head=t.next
        else:
            while(t!=None and t.data!=new_data):
                prev=t
                t=t.next
            if(t!=None):
                prev.next=t.next
        if(t is None):
                addfirst(new_data)       

    def printlist(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next
