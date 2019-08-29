import json
import datetime
with open("/home/admin1/Desktop/commercial.json",'r') as f:
    stock=json.load(f)
    print(type(stock) )
new_dict={} 
di={} 
def sellshare(name):
    for key,value in stock.items():
        for j in value:
            if (value.get(j)==name):
                new_dict.update(value)       
        for k in new_dict:
            if(k=="share_num"):
                t=new_dict[k]
                n=int(input("enter the no of shares you want to sell= "))
                s=new_dict[k]
                new_dict[k]=int(s)-n
                di={key:new_dict}
      

def buyshare(name):
      
    for key,value in stock.items():
        for j in value:
           if (value.get(j)==name):
                new_dict.update(value)       
        print(new_dict)            
        for k in new_dict:
            if(k=="share_num"):
                t=new_dict[k]
                n=int(input("enter the no of shares you want to buy?= "))
                new_dict[k]=n+int(t)
                print(new_dict)
    di={key:new_dict}
    stock.update(di)


def printlist():
    print(stock)
    for key,value in stock.items():
        print()
        for j,k in value.items():
            print(j,k,end=' ')



#driver code 
n=int(input("1.enter 1 to buy shares'\n' 2.enter 2 to sell shares'\n' 3.enter 3 to save the updated list into the database'\n'"))
name=input("enter the name whose record is to be updated= ")
if(n==1):
    buyshare(name)
if(n==2):
    sellshare(name)  
printlist()                      
# with open("/home/admin1/Desktop/commercial.json",'w') as f:
#     json.dump(stock,f)