# Maintain the Stock Symbol Purchased or Sold in a Stack implemented using
# Linked List to indicate transactions done.

import StockAccountStackBL as sb
s=sb.Stack()
for i in range(1,5):

    i=int(input("1.enter 1 to print the stock record of the company\n2.enter 2 to buy any stock\n3.enter 3 to pop the first stock in the record\n4.enter 4 to sell any stock 5.enter 5 to print the updated stock file\n6.enter 6 to exit the operation\n"))
    if(i==1):
            s.push()
            s.print_stack()    
            continue

    if(i==2):
            stock= input("enter the stock symbol you want to update= ")
            s.update_stock_file(stock)
            
    if(i==3):
        print("the first stock symbol popped out is= ",s.pop())    
        print("the stack of the stock symbols is= ")    
        s.print_stack()

    if(i==4):
        stock=input("enter the stock symbol you want to sell= ")
        if(s.check_key(stock)):
            s.sold(stock)
            print("the remaining stock_symbols are= ")
            s.print_stack()
        else:
            print("invalid record") 

    if(i==5):
        print(s.stock_symbol)

    if(i==6):
        exit()    
