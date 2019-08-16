# To the Util Class add temperaturConversion static function,
# given the temperature in fahrenheit as input outputs the temperature 
# in Celsius or viceversa using the formula
# Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
# Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C

class TempConv:
    def convert():
        celsius=float(input("enter the temperature in celsius= "))
        celToFahren= (celsius*9/5)+32
        print("the temperature when converted to fahrenheit is= ",celToFahren)
        fahrenheit=float(input("enter the temperature in fahrenheit= "))
        fahrenToCel=(fahrenheit-32)*5/9
        print("the temperature when converted to celsius is= ", fahrenToCel)

# driver code is
TempConv.convert()