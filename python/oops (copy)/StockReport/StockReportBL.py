# ----------------------------------StockReport prg-----------------------------------------------
# StockReport.py
# date : 27/08/2019
# method to print the stock report.


class StockPortFolio:

    def extract_record(self,stock_dict):

#retrieving the key-value pairs in stock dictionary

    for key,value in stock_dict.items():
        stockvalue=1
        print(value)
#printing the values(which are stored as nested dictionary for the customer details of each customer in the record) within the stock dictionary 
        for j in value:                 #we retrieve the keys of the nested dictionary
           
            if(j=='share_num'):         #if the key value is share_num we ask the user 
                if he wants to update his number of shares  
                new_count=int(input("enter the number of shares if you want to update the shares you own?= "))
                
                if(new_count==0):
                    share_count=value.get(j)         #if he doesn't then the share_num is fetched from
                    stockvalue*=int(share_count)     # the stock record in json file updating the price of the stock
                    print("the number of shares of the stock is= ",stockvalue) 

                else:
                    stockvalue*=new_count    #updating the price of the stock
                    print("the number of shares of the stock is= ",new_count) 
            if(j=='share_price'):
                price=value.get(j)
                print("the share price of the stock is= ",price)
#printing the total price of the stock by printing the product of the share price and the number of shares owned                    
                print("the total stock price of the stock is= ",stockvalue*int(price)) 

#printing the list of the stocks in the stockportfolio file

#===================================================================================================#

    def print_stocklist(self,stock_dict):
        for key,value in stock_dict.items():
            if(key=="stock_name1"or key=="stock_name2"or key=="stock_name3"):
                print(stock_dict.get(key))
               

