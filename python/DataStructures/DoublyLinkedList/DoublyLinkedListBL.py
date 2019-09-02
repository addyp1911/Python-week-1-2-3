
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
      
    def insertfirst(self,data):
        new_node=Node(data)
        new_node.prev=None
        new_node.next=self.head
        if(self.head is None):
            self.head=new_node
            return
        self.head.prev=new_node
        self.head=new_node
        
    def insertlast(self,data):
        new_node=Node(data)
        new_node.next=None
        if(self.head is None):
            new_node.prev=self.head
            self.head=new_node
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp.next
        
    def removefirst(self):
        if(self.head is None):
            print("the list is empty")
            return
        self.head=self.head.next
        self.head.prev=None
        
    def removelast(self):
        temp=self.head
        prev=None
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next=None
        
    def addafternode(self,prev_node,data):
        new_node=Node(data)
        if(prev_node is None):
            print("the previous node cant be none")
            return 
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if(new_node.next is not None):
            new_node.next.prev=new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,",")
            temp=temp.next
