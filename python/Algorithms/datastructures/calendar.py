# Write a program Calendar.java that takes the month and year as command-line arguments 
# and prints the Calendar of the month. Store the Calendar in an 2D Array,the first dimension as
# the week of the month and the second dimension stores the day of the week. 
# Print the result as following.
day_name=['su',' m',' t',' w',' t','fr','sa']
days=[31,28,31,30,31,30,31,31,30,31,30,31]
month=[]

def dayOfWeek(d,m,y):
        y0=y-(14-m)//12
        x=y0+y0//4-y0//100+y0//400
        m0=m+12*((14-m)//12)-2
        d0=(d+x+ 31*m0//12)% 7
        return d0

def isLeapYear(year):
    if((year%4==0) or(year%400==0 and year%100!=0)):
        c.days[1]=29



def cal():
    a=[]  
    for i in range(7):
        a.append(day_name[i]) 
    month.append(a)    
    for j in range(6):
        month.append([]) 
        
        
                
def update(start,month_no):
    k=0
    p=1
    
    for i in range(1,2):
        for j in  range(7):
            if(k<start):
                month[i].append('  ')
            else: 
                p1=str(p)+' '
                month[i].append(p1)
                p+=1
                
            k+=1  
    for i in range(2,7):
        for j in range(7):
            if(p<=days[month_no]):
                if(p<10):
                    p1=str(p)+' '
                    month[i].append(p1)
                else:
                    month[i].append(p)    
                p+=1
    

def display():
    for i in range(len(month)):
        for j in range(len(month[i])):
            print(month[i][j],end=" ")  
        print()
#driver code
 
mon=int(input("month no= "))   
year=int(input("year= "))
if(isLeapYear(year)):
    print("it is a leap year")
start=dayOfWeek(1,mon,year)         
cal()
update(start,mon)
display()

    