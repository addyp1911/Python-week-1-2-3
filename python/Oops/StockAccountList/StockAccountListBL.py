# ----------------------------------StockAccountList prg-----------------------------------------------
# StockAccountList.py
# date : 29/08/2019
# method to print the stock account details of company using linked list

#defining a node class
import json
class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class StockAccountList:
    def __init__(self):
        with open("stock.json",'r') as f:
            self.stock_file=json.load(f)
        self.head=None 
        self.size=0   

    def add_node(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def delete_node(self,name):
        temp=self.head
        prev=None
        while(temp):
            if(temp.data["name"]==name and temp==self.head):
                self.head=self.head.next
            elif(temp.data["name"]!=name and temp!=None):
                prev=temp
            elif(temp.data["name"]==name and temp!=None):
                prev.next=temp.next
            else:
                print("the name not found in the stock file!")
                return
            temp=temp.next 
        self.size-=1            

    def print_stock_file(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def update_stock_file(self,index,key):
        temp=self.head
        count=0
        while(temp):
            if(count==index):
                if(temp.data[key] is not None):
                    new_value=input("enter the new details= ")
                    temp.data[key]=new_value
            temp=temp.next
            count+=1
  
