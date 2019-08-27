# 3. Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

import LeapYearBL

try:
    year=int(input("enter the year"))
    LeapYearBL.checkleapyear(year)
    
except(TypeError):
    print("user please enter the valid year in integer format")    
