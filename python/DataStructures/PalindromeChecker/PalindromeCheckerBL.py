class Node:
    def __init__(self, data):
          self.data = data
          self.next=None
class Deque:
    def __init__(self):
          self.head=None
          self.size=0

    def append(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return 
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=new_node
        self.size+=1
        

    def appendLeft(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return 
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def pop(self):
        t=self.head
        prev=None
        while(t.next!=None):
            prev=t
            t=t.next
        prev.next=t.next
        return t.data    

         
    def popLeft(self,index):
        t=self.head
        count=-1
        while(t):
            count+=1
            if(count==index):
                prev=t
                t=t.next
                self.head=t
                break
        return prev.data   
      

    def palindromeChecker(self):
        f=True
        for i in range(0,dq.size//2):
          
            if(dq.pop()!=dq.popLeft(i)):
                f=False
                break    

        if(f):
            print("the string is palindrome")
        else:
            print("not a palindrome")    


       

    def printList(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next        