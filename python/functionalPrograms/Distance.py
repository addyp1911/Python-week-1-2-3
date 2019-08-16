class Distance:
    x=int(input("enter the x coordinate of the point"))
    y=int(input("enter the y coordinate of the point"))
    distance= pow((x**2+ y**2),0.5)
    print("the euclidean distance of the point is",distance)