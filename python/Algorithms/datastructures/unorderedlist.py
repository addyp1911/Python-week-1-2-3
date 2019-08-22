# Desc -> Read the Text from a file, split it into words and arrange it as Linked List. 
# Take a user input to search a Word in the List. 
# If the Word is not found then add it to the list, and if it found then remove the word from the List. In the end save the list into a file
# I/P -> Read from file the list of Words and take user input to search a Text
# Logic -> Create a Unordered Linked List. The Basic Building Block is the Node Object.
# Each node object must hold at least two pieces of information.
# One ref to the data field and  second the ref to the next node object.
# O/P -> The List of Words to a File.
class Node:
    def __init__(self,data):
          self.data = data
          self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def addFirst(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def addLast(self,data):
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
                ll.addFirst(new_data)       

    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next


#driver code
ll=LinkedList()
file1=open(r"/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()
for i in file_content:
    ll.addFirst(i)
ll.printList()    
string=input("enter the string to be searched= ")
ll.remove(string)
ll.printList()    
