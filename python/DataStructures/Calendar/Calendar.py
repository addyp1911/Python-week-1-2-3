# Write a program Calendar.java that takes the month and year as command-line arguments 
# and prints the Calendar of the month. Store the Calendar in an 2D Array,the first dimension as
# the week of the month and the second dimension stores the day of the week. 
# Print the result as following.
import CalendarBL as cb
 
mon=int(input("month no= "))   
year=int(input("year= "))
if(cb.isleapyear(year)):
    print("it is a leap year")
start=cb.dayofweek(1,mon,year)         
cb.cal()
cb.update(start,mon)
cb.display()

    