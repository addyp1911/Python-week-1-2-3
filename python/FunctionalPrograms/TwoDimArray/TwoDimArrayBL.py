
# ----------------------------------TwoDimArray prg-----------------------------------------------
#TwoDimArray.py
# date : 26/08/2019
# method to print a two dimensional array to standard output into a file.


def display(row,col):
    matrix=[]                                      #empty list is initialised
    for i in range(0,row):
        a=[]
        for j in range(0,col):
            num= int(input("enter the number= "))
            a.append(num)
        matrix.append(a)
    file1 = open("/home/admin1/Desktop/sample.txt","w")       #the file is opened in the write mode and outputstream is established
    for i in matrix:
        file1.write(' '.join(str(elem) for elem in i)) 
        file1.write('\n')