class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

       
class LinkedList:
    def __init__(self):
        self.head=None

    def adddata(self,data):
        new_node=Node(data)
        if(self.head is None):
            print("the list is empty")
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

    def removedata(self,name):
        t=self.head
        while(t.next.next!=None):
            if(t==None):
                return
            elif(t!=None and t.data==name):
                print(t,"kkkkkk")
                self.head=self.head.next
            else:
                while(t!=None and t.data!=name):
                    prev=t
                    t=t.next  
                prev.next=t.next
            t=t.next    
            
    def printlist(self):
        t=self.head
        while(t):
            print(t.data," ")
            t=t.next
     
                
            

ll=LinkedList()
ll.adddata("hey")
ll.adddata("hllo")
ll.adddata("bye")
ll.printlist()
ll.removedata("hllo")
ll.printlist()