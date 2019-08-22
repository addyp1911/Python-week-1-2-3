
class LeapYear:
   a=input("enter the year")
   year=int(a)
   if(year%4==0)or (year%400==0 and year%100!=0):
      print("user entered year is a leap year")
   else:   
      print("user entered year is not a leap year")