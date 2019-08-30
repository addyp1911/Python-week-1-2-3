# ----------------------------------StockAccountStack prg-----------------------------------------------
# StockAccountStack.py
# date : 29/08/2019
# method to print the stock account details of company using implemented stack

 

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class Stack:

    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=Node(data)
        temp=self.top
        if(temp is None):
            self.top=new_node
            return
        new_node.next=self.top
        self.top=new_node

#method for selling the shares of a particular company    
    def sold(self,key):
        temp=self.top
        prev=None
        while(temp):
            if(temp==None):
                print("the stack is empty")
                return
            if(temp==self.top and temp.data==key):
    
                self.top=self.top.next
            elif(temp is not None and temp.data!=key):
                  prev=temp
            else:
                prev.next=temp.next

            temp=temp.next             
        
    def printkey(self):
        t=self.top
        while(t):
            print(t.data," ")
            t=t.next

#to update the stock file if a new record is added         
    def update(self,stock,shares,price,file):
        new_dict={stock:{"share_num":shares,"share_price":price}}
        file.update(new_dict)
        print(file)

#to pop the first element of the stack of stock symbols
    def pop(self):
        if(self.top is None):
            print("the stack is underflow")
        else:
            return self.top.data   
         
#to check whether a record is present in the stock file or not 
    def check_key(self,key,file):
        for k,v in file.items():
            if(k==key):
                return True      
        return False

