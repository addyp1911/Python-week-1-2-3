 #2D Array
 #a.Desc -> A library for reading in 2D arrays of integers, doubles, or booleans 
 # from standard input and printing them out to standard output.
 #b. I/P -> M rows, N Cols, and M * N inputs for 2D Array.
 #c. Logic -> create 2 dimensional array in memory to read in M rows and N cols 
 #d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter 
 #with OutputStreamWriter to print the output to the screen.

import TwoDimArrayBL
M=int(input("enter the number of rows in the array: "))
N=int(input("enter the number of columns in the array: "))  
TwoDimArrayBL.disp(M,N)    