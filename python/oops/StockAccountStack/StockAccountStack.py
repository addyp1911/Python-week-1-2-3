# Maintain the Stock Symbol Purchased or Sold in a Stack implemented using
# Linked List to indicate transactions done.

#  {
#   "Pepsi":{"share_num":"23","share_price":"3000"},"Metroshoes":{"share_num":"15","share_price":"1500"},
#   "Maybelline":{"share_num":"50","share_price":"2000"}
#   }


import StockAccountStackBL as sb

import json
with open("/home/admin1/Desktop/commerciallist.json",'r') as f:
    stock_symbol=json.load(f)

s=sb.Stack()

for i in range(1,5):

    i=int(input("1.enter 1 to print the stock record of the company\n2.enter 2 to buy any stock\n3.enter 3 to pop the first stock in the record\n4.enter 4 to sell any stock 5.enter 5 to print the updated stock file\n6.enter 6 to exit the operation\n"))
    if(i==1):
        for k,v in stock_symbol.items():
            s.push(k)
        s.printkey()    
        continue

    if(i==2):
            stocksymbol=input("enter the stock symbol whose shares are purchased ") 
            shares=input("enter the number of shares bought= ") 
            price=input("enter the share price= ")
            print("the updated stock file is: ")
            s.update(stocksymbol,shares,price,stock_symbol)

    if(i==3):
        print("the first stock symbol popped out is= ",s.pop())    
        print("the stack of the stock symbols is= ")    
        s.printkey()

    if(i==4):
        stock=input("enter the stock symbol you want to sell= ")
        if(s.check_key(stock,stock_symbol)):
            s.sold(stock)
            print("the remaining stock_symbols are= ")
            s.printkey()
        else:
            print("invalid record") 

    if(i==5):
        print(stock_symbol)

    if(i==6):
        exit()    
