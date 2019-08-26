# ----------------------------------Distance prg-----------------------------------------------
# Distance.py
# date : 22/08/2019
# method to measure the distance using the formulae distance = sqrt(x*x + y*y). Use Math.power function

def calculateDistance(x,y):
    
    distance= pow((x**2+ y**2),0.5)
    print("the euclidean distance of the point is",distance)
