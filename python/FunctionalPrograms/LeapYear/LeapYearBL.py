
# ----------------------------------LeapYear prg-----------------------------------------------
# LeapYear.py
# date : 26/08/2019
# method to print whether the user entered year is a leap year

def checkleapyear(year):
    if(year%4==0) or (year%400==0 and year%100!=0):
        print("user entered year is a leap year")
    else:   
        print("user entered year is not a leap year")