# Simulate Banking Cash Counter
# Desc -> Create a Program which creates Banking Cash Counter where people come in
# to deposit Cash and withdraw Cash. 
# Have an input panel to add people to Queue to either deposit or withdraw money 
# and dequeue the people. Maintain the Cash Balance.
# I/P -> Panel to add People to Queue to Deposit or Withdraw Money and dequeue 
# Logic -> Write a Queue Class to enqueue and dequeue people to either deposit or withdraw money 
# and maintain the cash balance

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
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
        cc.dequeue()

    def withdraw(self,cash,balance):
        if(balance>=10000 and cash<=balance):
            balance-=cash
            print("the resultant cash balance is= ",balance)
        else:
            print("the balance is not sufficient")        
        cc.dequeue()

# driver code
cc=queue()
num=int(input("enter the no of people wanting to withdraw or deposit= "))
for i in range(1,num+1):
    balance=int(input("enter the balance of the person= "))
    cc.enqueue(i)
    string=input("enter 'd' for depositing money and 'w' for withdrawing money")
    if(string=='d'):
        cash=int(input("enter the amount to be deposit= "))
        cc.deposit(cash,balance)
    else:
            cash=int(input("enter the amount to be withdraw= "))
            cc.withdraw(cash,balance)
   






