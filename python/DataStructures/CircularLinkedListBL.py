class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
  
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addfirst(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
            return
        new_node.next=self.head
        self.head=new_node
        self.tail.next=self.head

    def addlast(self,data):
        new_node=Node(data)
        temp=self.head
        while(temp.next!=self.head):
            temp=temp.next
        temp.next=new_node
        self.tail=new_node
        self.tail.next=self.head

    def removefirst(self):
        if(self.head is None):
            print("the list is empty")
            return
        self.head=self.head.next
        self.tail.next=self.head

    def removelast(self):
        temp=self.head
        while(temp.next.next!=self.head):
            temp=temp.next
        self.tail=temp  
        self.tail.next=self.head


    def printlist(self):
        temp=self.head
        while(temp.next!=self.head):
            print(temp.data)
            temp=temp.next
        print(temp.data)
