# ---------------------------------- AnagramQueue prg-----------------------------------------------
# AnagramQueue.py
# date : 26/08/2019
# method to store only the anagram primes by implementing a queue

class Node:
    def __init__(self, data):
          self.data = data
          self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None    

    def enqueue(self,data):
        new_node=Node(data)
        if(self.front is None):
            self.front=new_node 
            return
        temp=self.front
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        self.rear=new_node

    def dequeue(self):
        temp=self.front
        if(self.front is None):
            print("the list is empty")
            return
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        self.rear=temp        
       
    def isanagram(self,num1,num2):
        n1=str(num1)
        n2=str(num2)
        x=sorted(n1)
        y=sorted(n2)
        return x==y

    def isprime(self,num):
        for i in range(2,num//2):
            if(num%i==0):
                return False
        return True

    def printlist(self):
        temp=self.front
        while(temp):
            print(temp.data)
            temp=temp.next
    
       