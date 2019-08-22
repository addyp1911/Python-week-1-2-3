import string
class Node:
    def __init__(self,data):
          self.data=data
          self.next=None
          self.prev=None

class DoublyLinkedList:
    def __init__(self):
          self.head=None
          self.tail=None

    def addFirst(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            self.tail=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def  addLast(self,data):
        new_node=Node(data)
        if(self.head is None):
           print("the list is empty ")
           return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node
        new_node.prev=t

    def addAtPosition(self,data,position):
        new_node=Node(data)
        if(position<1):
            print("the position is invalid")
        elif(position==1):
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            count=1 
            t=self.head
            while(count<position-1):
               t=t.next
            current=t.next
            t.next=new_node
            new_node.next=t

    def removeLast(self):
        t=self.head
        prev=None
        while(t.next!=None):
            prev=t
            t=t.next
        prev.next=None 

    def removeAtPosition(self,position):
        
        if(position<1):
            print("the position is invalid")
        elif(position==1):
            self.head=self.head.next
        else:
            count=1
          
            while(count<position-1):
                t=self.head
                t=t.next
                self.head=t
            current=t.next
            t.next=current.next
            current.next=None


    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

    def removeByKey(self,new_data):
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
                print('the element not found')       

#driver code
ar= DoublyLinkedList()
with open ("/home/admin1/Desktop/sample.txt",'r') as f:
    punc= string.punctuation  
    string=f.read()
    list1=''.join(elem for elem in string if not elem in punc).split()
    for i in list1:
        ar.addFirst(i)
    
    ar.removeLast()
    ar.addLast('pooja')
    ar.addFirst('bye')
    # ar.removeAtPosition(3)
    # ar.addAtPosition("pooja",6)
    ar.removeByKey("rakshita")
    ar.printList()
   
 
