import math as m
class BinaryTree:
    def countNumber(num):
        no_of_nodes=m.factorial(2*num)//m.factorial(num+1)*m.factorial(num)
        print(no_of_nodes)

    n=int(input("enter the number of nodes in the binary tree"))
    countNumber(n)    