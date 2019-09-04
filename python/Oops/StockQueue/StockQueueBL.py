class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
      

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

#method to add new stocks to the queue
    def enqueue(self,data):

        new_node=Node(data)
        if(self.front is None):
            self.front=new_node
            self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
        self.size+=1
 
#method to remove the stock symbol from queue if that stock is sold
    def dequeue(self,key):
        temp=self.front
        prev=None
        if(temp is None):
            print("the file is empty!")
            return
        while(temp.next):
            if(temp==self.front and temp.data==key):
                self.front=self.front.next
            elif(temp!=None and temp.data!=key):
                prev=temp
            else:
                prev.next=temp.next
            temp=temp.next

#printing the stock symbols in the queue
    def printqueue(self):
        temp=self.front
        while(temp is not None):
            print(temp.data)
            temp=temp.next

#method to buy new stocks if not present in the stockfile and the existing stockfile is updated
    def buystock(self,stockfile):
        stocksymbol=input("enter the stock name= ")
        share_price=input("enter the share price= ")
        share_num=input("enter the number of shares you wish to purchase= ")
        new_dict={stocksymbol:{"share_num":share_num,"share_price":share_price}}
        stockfile.update(new_dict)
        q.enqueue(stocksymbol)
        q.printqueue()

#method to check if that stock is already present in the stockfile

    def check_stock(self,key,stockfile):
        for k,v in stockfile.items():
            if(k==key):
                return True      
        return False

q=Queue()
q1=Queue()
