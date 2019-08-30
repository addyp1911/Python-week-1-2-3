import json
#  {
#   "stock_symbol1":{"stock_name":"pepsi","share_num":"23","share_price":"3000"}
# }
with open("/home/admin1/Desktop/commercial.json",'r') as f:
    stock_symbol=json.load(f)
    print(stock_symbol)
lst=[]
for k,v in stock_symbol.items():
    for j in v:
        if(v.get(j)=='pepsi'):
            lst.append(j)
for i in lst:
    del stock_symbol[k] 
print(stock_symbol)                
