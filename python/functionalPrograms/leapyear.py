
class LeapYear:
               a=input("enter the year")
               year=int(a)
               if(year%4==0)|(year%400==0 & year%100!=0):
                  print("user entered year is a leap year")
               else:   
                 print("user entered year is not a leap year")