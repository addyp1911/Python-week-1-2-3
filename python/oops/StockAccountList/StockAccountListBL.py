# ----------------------------------StockAccountList prg-----------------------------------------------
# StockAccountList.py
# date : 29/08/2019
# method to print the stock sccount details of company using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

       
class StockAccount:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node


    def delete_node(self, key): 

        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return 
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
        if(temp == None): 
            return 
        prev.next = temp.next 
  
        temp = None 

    def new_dict(self,stock_file):
        newdict={}
        temp=self.head
        while(temp):
            key=temp.data
            value=ll.retrieve_from_orig_dict(key,stock_file)
            newdict.update({key:value})
            temp=temp.next
        return newdict   

    def retrieve_from_orig_dict(self,key,stock_file):
        for k,v in stock_file.items():
            if(k==key):
                value=stock_file.get(k)
                return value 
         


    def printkey(self):
        t=self.head
        while(t):
            print(t.data," ")
            t=t.next
     
    def update(self,key,change_var,file):
        t=self.head
        while(t.next!=None):
            if(t.data==key):
                for k,v in file.items():
                    if(k==key):
                        for j in file[k]:
                            if(j==change_var):
                                new=input("enter the new value= ")
                                file[k][j]=new 
                                return file
            t=t.next 



    def check_key(self,key,file):
        for k,v in file.items():
            if(k==key):
                return True      
        return False
ll=StockAccount()    