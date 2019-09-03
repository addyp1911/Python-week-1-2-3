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
        
        
    def split(self):
    n1=self.head
    n2=self.head
    while(n1.next.next!=self.head and n1.next!=self.head):
        n2=n1.next
        n1=n1.next.next

    if(n1.next.next==self.head):
        n1=n1.next
    head1=self.head
    head2=n2.next
    n1.next=head2
    n2.next=head1
    cl.printlist(head1)
    cl.printlist(head2)
    
