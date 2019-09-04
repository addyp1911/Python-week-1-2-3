# ----------------------------------OrderedLinkedList prg-----------------------------------------------
# OrderedLinkedList.py
# date : 26/08/2019
# method to implement an orderedlinked list
class Node:
    def __init__(self,data):
          self.data = data
          self.next=None

class OrderedLinkedList:
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
<<<<<<< HEAD
=======
        temp=self.head
>>>>>>> 8fe8be723c476187e1b13f5f22e9069af8611f62
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
<<<<<<< HEAD
            temp=temp.next
=======
            temp=temp.next
>>>>>>> 8fe8be723c476187e1b13f5f22e9069af8611f62
