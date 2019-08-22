

class PowerOf2:
    a=input("enter the highest power of 2 ")
    num=int(a) 
    i=0
    sum=0
    while(i<=num):
        sum+=pow(2,i)
        i=i+1 
    print(sum)