
# Desc -> Write a program to read in Stock Names, Number of Share, Share Price.
# Print a Stock Report with total value of each Stock and the total value of Stock.
# b. I/P -> N number of Stocks, for Each Stock Read In the Share Name, Number of
# Share, and Share Price
# c. Logic -> Calculate the value of each stock and the total value
# d. O/P -> Print the Stock Report.
# Hint -> Create Stock and Stock Portfolio Class holding the list of Stocks read
# from the input file. Have functions in the Class to calculate the value of each
# stock and the value of total stocks

import json
import StockReportBL as sr
with open("/home/admin1/Desktop/stock.json",'r') as f:
    stock_dict=json.load(f)
    obj=sr.StockPortFolio()
    obj.extract_record(stock_dict)
    obj.print_stocklist(stock_dict)
