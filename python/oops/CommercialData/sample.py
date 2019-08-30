import datetime
import json
# with open("",'r') as f:
#     stockfile=json.load(f)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
      

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enqueue(self,data):

        new_node=Node(data)
        if(self.front is None):
            self.front=new_node
            self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
        self.size+=1

    def dequeue(self):
        temp=self.front
        prev=None
        while(temp):
            prev=temp
            temp=temp.next
        self.rear=prev  
        prev.next=temp.next
        self.size-=1

    def printlist(self):
        while(self.front!=self.rear):
            print(self.front.data)
            self.front=self.front.next
            

q=Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
q.printlist()
q.dequeue()
q.printlist()


