# ----------------------------------CommercialData prg-----------------------------------------------
# CommercialData.py
# date : 30/08/2019
#The StockAccount class also maintains a list of CompanyShares object which has
# Stock Symbol and Number of Shares as well as DateTime of the transaction.

import json
import CommercialDataBL as cd
with open("/home/admin1/Desktop/commerciallist.json",'r') as f:
    stock_file=json.load(f)

for i in range(1,4):
    i=int(input("1.enter 1 to print stock record\n2.enter 2 to buy shares of stock\n3.enter 3 to sell shares of the stock\n4. enter 4 to exit the application\n"))    
    if(i==1):
        cd.s.print_report(stock_file)
        continue    
    if(i==2):
        stock_symbol=input("enter the stock symbol whose shares you want to purchase= ")
        cd.s.buy_share(stock_symbol,stock_file)
        continue 
    if(i==3):
        stock_symbol=input("enter the stock symbol whose shares you want to sell= ")
        cd.s.sell_share(stock_symbol,stock_file)
        continue 
    if(i==4):
        exit()

with open("/home/admin1/Desktop/commerciallist.json",'w') as f:
    json.dump(stock_file,f)