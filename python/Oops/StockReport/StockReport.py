# Desc -> Write a program to read in Stock Names, Number of Share, Share Price.
# Print a Stock Report with total value of each Stock and the total value of Stock.
# b. I/P -> N number of Stocks, for Each Stock Read In the Share Name, Number of
# Share, and Share Price
# c. Logic -> Calculate the value of each stock and the total value
# d. O/P -> Print the Stock Report.
# Hint -> Create Stock and Stock Portfolio Class holding the list of Stocks read
# from the input file. Have functions in the Class to calculate the value of each
# stock and the value of total stocks

import StockReportBL as sr
obj=sr.StockPortFolio()
obj.total_stock_price()
obj.print_stock_file()

