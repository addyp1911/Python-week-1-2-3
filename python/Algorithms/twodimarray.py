class matrix:
      def twodim():
              matrix=[]
              i=int(input("enter the no of rows= "))
              j=int(input("enter the no of columns= "))
              for p in range(0,i):
                A=[]
                for k in range(0,j): 
                        a=int(input("enter the value to be entered= "))
                        A.append(a)  
                matrix.append(A)
                for  i in matrix:
                    print(','.join(str(elem) for elem in i))
# driver code
matrix.twodim()
      