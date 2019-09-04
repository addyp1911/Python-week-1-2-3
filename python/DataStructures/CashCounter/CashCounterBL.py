# ---------------------------------CashCounter prg-----------------------------------------------
# BinarySearchFileRead.py
# date : 26/08/2019
# method to execute the cash counter program by implementing a queue


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None


    def enqueue(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        new_node.next=t

    def dequeue(self):
        t=self.head
        if(self.head is None):
            print("the queue is empty")
            return
        obj=t.data
        t=t.next
        return obj    

    def deposit(self,cash,balance):
        balance+=cash
        print("the resultant cash balance is= ",balance)
        dequeue()

    def withdraw(self,cash,balance):
        if(balance>=10000 and cash<=balance):
            balance-=cash
            print("the resultant cash balance is= ",balance)
        else:
            print("the balance is not sufficient")        
            dequeue()

# driver code