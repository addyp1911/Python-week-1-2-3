# The StockAccount class also maintains a list of CompanyShares object which has
# Stock Symbol and Number of Shares as well as DateTime of the transaction. When
# buy or sell is initiated StockAccount checks if CompanyShares are available and
# accordingly update or create an Object.
# 6. Maintain the List of CompanyShares in a Linked List So new CompanyShares can
# be added or removed easily. Do not use any Collection Library to implement Linked
# List

import StockAccountListBL as cd
import json
with open("/home/admin1/Desktop/commerciallist.json",'r') as f:
    stock_file=json.load(f)


for i in stock_file:
    cd.ll.add_node(i)

cd.ll.printkey()

update_key=input("enter the record key you would like to update?= ")
if(cd.ll.check_key(update_key)):
      update_value=input("enter the record atrribute you would like to update?= ")
      print(cd.ll.update(update_key,update_value))
else:
    print("invalid key") 

user_key=input("enter the node you would like to delete?= ")

if(cd.ll.check_key(user_key)): 
    cd.ll.delete_node(user_key)

print("the modified dictionary is= ",cd.ll.new_dict(stock_file))    
