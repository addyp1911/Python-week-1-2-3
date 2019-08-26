# ----------------------------------TwoDimArray prg-----------------------------------------------
# TwoDimArray.py
# date : 26/08/2019
# method to enter a two dimensional array
def printArray(row,col):  
    matrix=[]               #empty list initiliased
    for p in range(0,row):
            A=[]
    for k in range(0,col): 
            a=int(input("enter the value to be entered= "))
            A.append(a)  
    matrix.append(A)
    for  i in matrix:
        print(','.join(str(elem) for elem in i))
        print('\n')   
