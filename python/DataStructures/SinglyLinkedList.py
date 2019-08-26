class Node:
    def __init__(self, data):
          self.data = data
          self.next = None
          
  # Linked List class contains a Node object
class LinkedList:
  
	# Function to initialize head 
    def __init__(self):
      self.head=None
    
    def addFirst(self,data):
        new_node= Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def addLast(self,data):
        new_node=Node(data)
        if(self.head is None):
            head=new_node
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node
               
    def insertAfter(self,prev_node,data):
        new_node=Node(data)
        if(prev_node==None):
            print("the previous node value should be there ")
        t=prev_node.next
        prev_node.next=new_node
        new_node.next=t    

    def removeFirst(self):
        data=self.head.data
        head=self.head.next

    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

    #driver code

if __name__=='__main__': 


    ls = LinkedList() 
    ls.addFirst(6) 
    ls.addFirst(7) 
    ls.addLast(9)
    ls.addLast(4)
    ls.printList()
    ls.insertAfter(ls.head.next, 8)
    ls.printList() 
    
        
        

