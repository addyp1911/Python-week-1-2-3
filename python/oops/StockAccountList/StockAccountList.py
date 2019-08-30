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

#adding keys to linked list
for i in stock_file:
    cd.ll.add_node(i)

cd.ll.printkey()

#asking for user to update any customer detail
update_key=input("enter the record key you would like to update?= ")

if(cd.ll.check_key(update_key,stock_file)):
      update_value=input("enter the record attribute you would like to update?= ")
      print(cd.ll.update(update_key,update_value,stock_file))
# new record being added to the stock file if the key is not present in it
else:
        name=input("enter the shareholder name= ")
        stock=input("enter the stockname he wants to buy= ")
        price=input("enter the price of the stock= ")
        share_num=input("enter the number of shares he wants to buy= ")
        key=input("enter the key of this record= ")
        add_dict={key:{"name":name,"stock":stock,"price":price,"share_num":share_num}}
        stock_file.update(add_dict)
        print(stock_file)      
#asking the user if he would delete any record from the existing file
user_key=input("enter the node you would like to delete?= ")
if(cd.ll.check_key(user_key,stock_file)): 
    cd.ll.delete_node(user_key)
    #the modified stockfile is printed
    print("the modified stockfile is= ",cd.ll.new_dict(stock_file))  
  
