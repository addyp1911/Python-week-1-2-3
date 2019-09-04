# ----------------------------------PalindromeChecker prg-----------------------------------------------
# PalindromeChecker.py
# date : 26/08/2019
# method to check whether a string is a palindrome or not by implementing a deque 

class Node:
    def __init__(self, data):
          self.data = data
          self.next=None
class Deque:
    def __init__(self):
          self.front=None
          self.size=0

    def append(self,data):
        new_node=Node(data)
        if(self.front is None):
            self.front=new_node
            return 
        t=self.front
        while(t.next!=None):
            t=t.next
        t.next=new_node
        self.size+=1
        

    def appendleft(self,data):
        new_node=Node(data)
        if(self.front is None):
            self.front=new_node
            return 
        new_node.next=self.front
        self.front=new_node
        self.size+=1

    def pop(self):
        t=self.front
        prev=None
        while(t.next!=None):
            prev=t
            t=t.next
        prev.next=t.next
        return t.data    

         
    def popleft(self,index):
        t=self.front
        count=-1
        while(t):
            count+=1
            if(count==index):
                prev=t
                t=t.next
                self.front=t
                break
        return prev.data   
      

    def palindromechecker(self):
        f=True
        for i in range(0,self.size//2):
          
            if(self.pop()!=self.popleft(i)):
                f=False
                break    

        if(f):
            print("the string is palindrome")
        else:
            print("not a palindrome")    


       

    def printlist(self):
        t=self.front
        while(t):
            print(t.data)
            t=t.next        
