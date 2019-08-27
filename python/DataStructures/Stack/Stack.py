#implementing a stack to perform push and pop operations

import StackBL as sb
s=sb.Stack()
size=int(input("enter the size of the stack= "))
for i in range(size):
    data=int(input("enter the element to be added to the stack= "))
    s.push(data)
s.printstack()
print('popping the first element of the stack')
s.pop()
var=input("enter the element you want to pop= ")
s.pop(var)
s.printstack()
s.countsize()
var1=input("enter the element you want to search= ")
print(s.search(var1))
print("the first element in the stack is",s.peek())
