
# ----------------------------------DayOfWeek prg-----------------------------------------------
# DayOfWeek.py
# date : 26/08/2019
# method to find the day of the week using formulae for the gregorian calendar



def dayofweek(d,m,y):
    y0=y-(14-m)//12
    x=y0+y0//4-y0//100+y0//400
    m0=m+12*((14-m)//12)-2
    d0=(d+x+ 31*m0//12)% 7
    arr=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("the day of the week that date falls on is= ",arr[d0])