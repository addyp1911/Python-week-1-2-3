
class Node:
    def __init__(self, data):
          self.data = data
          self.next = None
          
  # Linked List class contains a Node object
class LinkedList:
  
	# Function to initialize head 
    def __init__(self):
      self.head=None
    
    def addfirst(self,data):
        new_node= Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def addlast(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node
               
    def insertafter(self,prev_node,data):
        new_node=Node(data)
        if(prev_node==None):
            print("the previous node value should be there ")
        temp=prev_node.next
        prev_node.next=new_node
        new_node.next=temp    

    def removefirst(self):
        if(self.head is None):
		print("the list is empty")
		return
        self.head=self.head.next
	
    def removelast(self):
	temp=self.head
	while(temp.next.next):
	    temp=temp.next
        temp.next=None		
	
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
