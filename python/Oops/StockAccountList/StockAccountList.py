# The StockAccount class also maintains a list of CompanyShares object which has
# Stock Symbol and Number of Shares as well as DateTime of the transaction. When
# buy or sell is initiated StockAccount checks if CompanyShares are available and
# accordingly update or create an Object.
# 6. Maintain the List of CompanyShares in a Linked List So new CompanyShares can
# be added or removed easily. Do not use any Collection Library to implement Linked
# List

import StockAccountListBL as sb
    sl=sb.StockAccountList()
    for records in sl.stock_file["stockaccount"]:
            sl.add_node(records)

    while(True):
        i=int(input("1.enter 1 to add a new person to stock file\n2.enter 2 to delete a person from the stockfile\n3.enter 3 to print the stockfile\n4.enter 4 to update the stockfile\n5.enter 5 to exit the application\n"))     
        if i==1:
            new_dict={}
            name=input("enter the name of the person =")
            stock=input("enter the stock symbol= ")
            shares=input("enter the shares= ")
            price=input("enter the share price= ")
            new_dict.update({"name":name,"stock":stock,"share":shares,"share_price":price})
            sl.add_node(new_dict) 

        elif i==2:
            name=input("enter the name of the person whose record you would delete= ")
            sl.delete_node(name)

        elif i==3:
            sl.print_stock_file() 

        elif i==4:
            index=int(input("enter the index of the record= "))
            if(index > sl.size or index < 0):
                print("invalid index!")
            else:    
                key=input("enter the attribute that needs to be updated= ")
                sl.update_stock_file(index,key)

        elif i==5:
            exit()
            break
                  
  
