 #2D Array
 #a.Desc -> A library for reading in 2D arrays of integers, doubles, or booleans 
 # from standard input and printing them out to standard output.
 #b. I/P -> M rows, N Cols, and M * N inputs for 2D Array.
 #c. Logic -> create 2 dimensional array in memory to read in M rows and N cols 
 #d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter 
 #with OutputStreamWriter to print the output to the screen.

class TwoDimArray:
    
    def input():
        M=int(input("enter the number of rows in the array: "))
        N=int(input("enter the number of columns in the array: "))
        matrix=[]
        for i in range(0,M):
            a=[]
            for j in range(0,N):
                num=int(input("enter the number= "))
                a.append(num)
            matrix.append(a)

        file1 = open("/home/admin1/Desktop/sample.txt","w")
        for i in matrix:
            file1.write(' '.join(str(elem) for elem in i)) 
            file1.write('\n')


    input()    