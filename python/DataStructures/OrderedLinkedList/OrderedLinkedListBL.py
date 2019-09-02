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
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node

    def sort(self):
        temp=self.head
        while(temp):
            new_temp=temp.next
            while(new_temp):
                if(temp.data>new_temp.data):
                    t=temp.data
                    temp.data=new_temp.data
                    new_temp.data=t
                new_temp=new_temp.next
            temp=temp.next    
    
    def removefirst(self):
        temp=self.head
        if(self.head is None):
            print("the list is empty")
            return
        self.head=self.head.next
     
    def removelast(self):
        temp=self.head
        if(self.head is None):
            print("the list is empty")
            return
        while(temp.next.next):
            temp=temp.next
        temp.next=None    
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
