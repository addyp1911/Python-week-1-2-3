# ----------------------------------TempConversion prg-----------------------------------------------
# TempConversion.py
# date : 26/08/2019
# method to convert the user entered temperature in celsius to fahrenheit and vice versa

def convert():

    celsius=float(input("enter the temperature in celsius= "))

    celToFahren= (celsius*9/5)+32

    print("the temperature when converted to fahrenheit is= ",celToFahren)

    fahrenheit=float(input("enter the temperature in fahrenheit= "))

    fahrenToCel=(fahrenheit-32)*5/9

    print("the temperature when converted to celsius is= ", fahrenToCel)