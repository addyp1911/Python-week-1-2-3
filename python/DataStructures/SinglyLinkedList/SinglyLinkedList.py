
#implementing a singlylinkedlist and asking the user to enter the data into it

import SinglyLinkedListBL as sl
ls = sl.LinkedList() 
size=int(input("enter the size of the linkedlist= "))
for i in range(size):
    data=input("enter the element= ")
    ls.addfirst(data)
ls.insertafter(ls.head.next, 8)
ls.printlist() 

        
        

