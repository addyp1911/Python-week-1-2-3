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

#new dictionary defined to modify the existing stock file after deletion of a particular record in it 
    def new_dict(self,stock_file):
        newdict={}     #initialising new dictionary
        temp=self.head        
        while(temp):           
            key=temp.data  
#method retrieve_from_orig_dict is used to retrieve a particular shareholder detail record using key            
            value=ll.retrieve_from_orig_dict(key,stock_file)
            newdict.update({key:value})
            temp=temp.next
        return newdict   

    def retrieve_from_orig_dict(self,key,stock_file):
        for k,v in stock_file.items():
            if(k==key):
                value=stock_file.get(k)
#the shareholder details corresponding to the particular key is returned                
                return value 
   
    def printkey(self):
        t=self.head
        while(t):
            print(t.data," ")
            t=t.next

#method to update any attribute(name,share_num,stock_name)of any shareholder in the stockfile     
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


#method to check whether a particular record is present in the stock file
    def check_key(self,key,file):
        for k,v in file.items():
            if(k==key):
                return True      
        return False

#creating the object        
ll=StockAccount()    