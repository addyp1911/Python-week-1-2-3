

class StockPortFolio:

    def extract_record(stock_dict):
           #retrieving the key-value pairs in stock dictionary
        for key,value in stock_dict.items():
            
#printing the values(which are stored as nested dictionary for the customer details of each customer in the record) within the stock dictionary 
            print(value)
            stock_value=1
            for j in value:                             #we retrieve the keys of the nested dictionary
    #if the key value is share_num we ask the user if he wants to update his number of shares             
                if(j=='share_num'):
                    new_count=int(input("enter the number of shares if you want to update the shares you own?= "))
                    if(new_count==0):
                        share_count=value.get(j)         #if he doesn't then the share_num is fetched from the stock record in json file 
                        stockvalue=int(share_count)     
                        print("the number of shares of the stock is= ",share_count) 

                    else:
                        stockvalue=new_count    
                        print("the number of shares of the stock is= ",new_count) 
                if(j=='share_price'):
                    price=value.get(j)
                    print("the share price of the stock is= ",price)
                    print("the total stock price of the stock is= ",stock_value*int(price))

    def print_stocklist(stock_dict):
        for key,value in stock_dict.items():
            if(key=="stock_name1"or key=="stock_name2"or key=="stock_name3"):
                print(stock_dict.get(key))
               

