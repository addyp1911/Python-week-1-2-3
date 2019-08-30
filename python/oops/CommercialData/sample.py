import json
with open("/home/admin1/Desktop/commerciallist.json",'r') as f:
    file=json.load(f)
    print(file)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

       
class StockList:
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

    def new_dict(self):
        di={}
        t=self.head
        while(t):
            print('hello')
            key=t.data
            value=ll.retrieve_from_orig_dict(key)
            di.update({key:value})
            t=t.next
        return di    

    def retrieve_from_orig_dict(self,key):
        for k,v in file.items():
            if(k==key):
                value=file.get(k)
                return value    



    def printkey(self):
        t=self.head
        while(t):
            print(t.data," ")
            t=t.next
     
    def update(self,key,change_var):
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
    def check_key(self,key):
        for k,v in file.items():
            if(k==key):
                return True      
        return False
       

ll=StockList()
for i in file:
    ll.add_node(i)
ll.printkey()
update_key=input("enter the record key you would like to update?= ")
if(ll.check_key(update_key)):
    update_value=input("enter the record atrribute you would like to update?= ")
    print(ll.update(update_key,update_value))
else:
    print("invalid key")    
user_key=input("enter the node you would like to delete?= ")
if(ll.check_key(user_key)): 
    ll.delete_node(user_key)
ll.printkey()    
print("the modified dictionary is= ",ll.new_dict())    
