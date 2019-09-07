# ----------------------------------StockAccountList prg-----------------------------------------------
# StockAccountList.py
# date : 29/08/2019
# method to print the stock account details of company using linked list

# my json file stockrecord
# {"shareholder1":{"name":"sonal k","stock":"HCL","shareprice":"2000","share_num":"30"},
#  "shareholder2":{"name":"jay s","stock":"E&Y","shareprice":"3000","share_num":"50"},
#  "shareholder3":{"name":"lata s","stock":"H&M","shareprice":"1500","share_num":"10"}
# }

#defining a node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#implementing a linked list with keys as nodes(keys are the record number as defined in the json file)       
class StockAccount:
    def __init__(self):
        self.head=None

#method to add the keys of the stockfile as nodes to the linked list
    def add_node(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node

#method to delete the specific node as entered by the user , using the key
    
    def delete_node(self,data):
        t=self.head
        while(t.next.next!=None):
            if(t==None):
                return
            elif(t!=None and t.data==data):
                self.head=self.head.next
            else:
                while(t!=None and t.data!=data):
                    prev=t
                    t=t.next  
                prev.next=t.next
            t=t.next 
#new dictionary defined to modify the existing stock file after deletion of a particular record in it 
    
  

#method to check whether a particular record is present in the stock file
    def check_key(self,key,file):
        for k,v in file.items():
            if(k==key):
                return True      
        return False

#creating the object        
ll=StockAccount()    