# ----------------------------------Stack prg-----------------------------------------------
# Stack.py
# date : 26/08/2019
# method to implement the stack with the library methods


class Node:
    def __init__(self,data):
          self.data=data
          self.next=None
class Stack:
    def __init__(self):
          self.head=None 
          self.size=0

    def push(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        self.size+=1

    def pop(self,data=None):
        if(data is None):
            if(self.head is None):
                print("the list is empty")
                return
            obj=self.head.data
            self.head=self.head.next
            self.size-=1
            return obj
        else:   
            temp=self.head
            while(temp!=None and temp.data!=data):
                prev=t
                temp=temp.next
            if(temp!=None):
                prev.next=temp.next 
            else:
                print("the number not found")  

    def peek(self):
        return self.head.data

    def countsize(self):
        print('the size of the stack is',self.size)


    def isempty(self):
        if(self.size==0):
            return True
        else:
            return False


    def search(self,data):
        temp=self.head
        count=self.size-1
        while(temp):
            if(temp.data==data):
                return count
            temp=temp.next
            count-=1
            
        return -1    

    def printstack(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
