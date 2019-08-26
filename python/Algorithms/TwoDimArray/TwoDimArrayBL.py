
def printArray(row,col):  
    matrix=[]
    for p in range(0,row):
            A=[]
    for k in range(0,col): 
            a=int(input("enter the value to be entered= "))
            A.append(a)  
    matrix.append(A)
    for  i in matrix:
        print(','.join(str(elem) for elem in i))
        print('\n')   
