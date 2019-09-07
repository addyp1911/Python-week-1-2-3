# ----------------------------------StockReport prg-----------------------------------------------
# StockReport.py
# date : 27/08/2019
# method to print the stock report.
import json
class StockPortFolio:

    def __init__(self):
        with open("Stock.json",'r') as f:
            self.stock_file=json.load(f)

    def print_stock_file(self):
        for record in range(len(self.stock_file["Stock Report"])):
            print(record,self.stock_file["Stock Report"][record])
  
    def total_stock_price(self):
        total_price=0
        for records in range(len(self.stock_file["Stock Report"])):
            for key,value in self.stock_file["Stock Report"][records].items():
                if(key =='Number of Share'):
                    total_price = self.stock_file["Stock Report"][records][key]
                if(key =='Share Price'):
                    total_price *= self.stock_file["Stock Report"][records][key] 
            print("the total stock price of "+self.stock_file["Stock Report"][records]["Stock Name"]+" is",total_price)