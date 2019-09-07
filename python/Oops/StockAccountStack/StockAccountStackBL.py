# ----------------------------------StockAccountStack prg-----------------------------------------------
# StockAccountStack.py
# date : 29/08/2019
# method to print the stock account details of company using implemented stack

import json
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class Stack:

    def __init__(self):
        self.top=None
        with open("Stock.json",'r') as f:
            self.stock_symbol=json.load(f)
  
#method for pushing the stock file data into the stack
    def push(self):
        for record in range(len(self.stock_symbol["Stock Report"])):
            data = self.stock_symbol["Stock Report"][record]
            new_node=Node(data)
            temp=self.top
            if(temp is None):
                self.top=new_node
            else:    
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
            if(temp==self.top and temp.data['Stock Name']==key):
                self.top=self.top.next
            elif(temp is not None and temp.data['Stock Name']!=key):
                  prev=temp
            else:
                prev.next=temp.next

            temp=temp.next             
        
    def print_stack(self):
        temp=self.top
        while(temp):
            print(temp.data," ")
            temp=temp.next


    def update_stock_file(self,stock):
        for record in range(len(self.stock_symbol["Stock Report"])):
            for key,value in self.stock_symbol["Stock Report"][record].items():
                if self.stock_symbol["Stock Report"][record][key]==stock:
                    new_share=input("enter the number of shares bought= ")
                    self.stock_symbol["Stock Report"][record]["Number of Share"]=new_share
                    new_share_price = input("enter the share price= ")
                    self.stock_symbol["Stock Report"][record]["Share Price"]=new_share_price
                    with open("stock.json",'w') as f:
                        json.dump(self.stock_symbol,f)
                    break
                else:
                    s.push()
#to pop the first element of the stack of stock symbols
    def pop(self):
        if(self.top is None):
            print("the stack is underflow")
        else:
            data=self.top.data
            self.top=self.top.next
            return data   
         
#to check whether a record is present in the stock file or not 
    def check_key(self,stock):
        for record in range(len(self.stock_symbol)):
             for key,value in self.stock_symbol["Stock Report"][record].items():
                if self.stock_symbol["Stock Report"][record][key]==stock:
                    return True      
        return False

