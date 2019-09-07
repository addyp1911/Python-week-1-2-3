# Further maintain DateTime of the transaction in a Queue implemented using Linked
# List to indicate when the transactions were done.

import datetime
import json
import StockQueueBL as sq

with open("Commerciallist.json",'r') as f:
    stockfile=json.load(f)


for i in range(1,5):

    i=int(input("1.enter 1 to print the stock record of the company\n2.enter 2 to buy any stock\n3.to sell any stock\n4.to print the updated stock file\n5.to exit the operation\n"))
    if(i==1):
        for k,v in stockfile.items():
            sq.q.enqueue(k)
        sq.q.printqueue()
        continue

    if(i==2):
            sq.q.buystock(stockfile)
            sq.q1.enqueue(str(datetime.datetime.now()))
            sq.q1.printqueue()
    if(i==3):
        stock=input("enter the stock symbol you'd sell= ")
        if(sq.q.check_stock(stock,stockfile)):
            sq.q.dequeue(stock)
        sq.q.printqueue()
        
    if(i==4):
        #printing the updated stock file and writing the updated stock records into the json file
        print(stockfile)
        with open("/home/admin1/Desktop/commerciallist.json",'w') as f:
               json.dump(stockfile,f)   

    if(i==5):
        exit()    



