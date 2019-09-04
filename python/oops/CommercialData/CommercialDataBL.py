# The StockAccount class also maintains a list of CompanyShares object which has
# Stock Symbol and Number of Shares as well as DateTime of the transaction. When
# buy or sell is initiated StockAccount checks if CompanyShares are available and
# accordingly update or create an Object.

#{"Pepsi": {"customer_name":"raksh s","share_num": "23", "share_price": "3000"},"Metroshoes": {"customer_name":"umang s","share_num": "15", "share_price": "1500"},"Maybelline": {"customer_name":"harsh s","share_num": "50", "share_price": "2000"}, 
#"Activa": {"share_num": "456", "share_price": "450"}}
class StockReport:

    def buy_share(self,stock_symbol,stock_file):
        for key,value in stock_file.items():
            if(key == stock_symbol):
                for val in value:
                    if(val=="share_num"):
                        s.add(val,value.get(val),stock_file,stock_symbol)
                
  
    def add(self,key,old_shares,file,stock):
        new_shares=int(input("enter the number of shares to be purchased= "))
        file[stock][key]=int(old_shares)+new_shares
     
        
    def sell_share(self,stock_symbol,stock_file):
        for key,value in stock_file.items():
            if(key == stock_symbol):
                for val in value:
                    if(val=="share_num"):
                        s.delete(val,value.get(val),stock_file,stock_symbol)

    def delete(self,key,old_shares,file,stock):
        shares=int(input("enter the number of shares to be sold= "))
        if(shares==old_shares):
            file[stock][key]=0
        elif(shares>int(old_shares)):
            print("the number of shares to be sold is more than present with the company")    
        else: 
            file[stock][key]=int(old_shares)-shares

    def print_report(self,stock_file):
        print("Stock ShareNo. SharePrice ")
        for key,value in stock_file.items():
            for val in value:
                if(val=="share_num"):
                    share_num=value.get(val)
                if(val=="share_price"):
                    share_price=value.get(val)
                if(val=="customer_name"):
                    customer=value.get(val)        
            print("{0} ,{1} , {2} , {3}".format(key,customer,share_num,share_price),end="\t")  
            print() 

s=StockReport()