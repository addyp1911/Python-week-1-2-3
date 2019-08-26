def disp(row,col):
    matrix=[]
    for i in range(0,row):
        a=[]
        for j in range(0,col):
            num=int(input("enter the number= "))
            a.append(num)
        matrix.append(a)
    file1 = open("/home/admin1/Desktop/sample.txt","w")    
    for i in matrix:
        file1.write(' '.join(str(elem) for elem in i)) 
        file1.write('\n')