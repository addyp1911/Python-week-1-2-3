# 3. Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

import LeapYearBL
a=input("enter the year")
year=int(a)
LeapYearBL.checkLeapYear(year)