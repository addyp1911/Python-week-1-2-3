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
i=input("1.type 1 for push\n2.type 2 for pop \n3.type 3 for printing the stack\n")
if(i==1):
    for k,v in stock_symbol.items():
        s.push(k)
    i=input("print or pop?= ")
    if(i==2):
        print("the first stock symbol popped out is= ",s.pop())    
        print("the stack of the stock symbols is= ")    
        s.printkey()

    elif(i==3):
        s.printkey() 


stocksymbol=input("enter the stock symbol whose shares are purchased ") 
shares=input("enter the number of shares bought= ") 
price=input("enter the share price= ")

print("the updated stock file is: ")
s.update(stocksymbol,shares,price,stock_symbol)

stock=input("enter the stock symbol you want to sell= ")
if(s.check_key(stock,stock_symbol)):
    s.sold(stock)
    print("the remaining stock_symbols are= ")
    s.printkey()
else:
    print("invalid record")

