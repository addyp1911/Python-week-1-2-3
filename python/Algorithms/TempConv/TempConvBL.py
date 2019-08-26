def convert():
    celsius=float(input("enter the temperature in celsius= "))
    celToFahren= (celsius*9/5)+32
    print("the temperature when converted to fahrenheit is= ",celToFahren)
    fahrenheit=float(input("enter the temperature in fahrenheit= "))
    fahrenToCel=(fahrenheit-32)*5/9
    print("the temperature when converted to celsius is= ", fahrenToCel)