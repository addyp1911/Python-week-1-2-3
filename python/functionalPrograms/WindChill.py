# Write a program WindChill.py that takes two double command-line arguments t and v and prints the wind chill. 
# Use Math.pow(a, b) to compute ab. 
#Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
# the National Weather Service defines the effective temperature (the wind chill) to be:
#Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 

class WindChill:
    def calculateWindChill(t,v):
        windChill=35.74+.6215*t+(0.4275*t-35.75)*pow(v,0.16)
        print(windChill)
    
#Driver Code
temp=int(input("enter the temperature in fahrenheit"))
windspeed=int(input("enter the windspeed in miles per hour"))
WindChill.calculateWindChill(temp,windspeed)        
