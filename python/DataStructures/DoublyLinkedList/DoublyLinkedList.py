import DoublyLinkedListBL as dbl
dl=dbl.DoublyLinkedList()

f=open("/home/admin1/Desktop/sample.txt",'r') 
string_list=f.read().split()
for i in string_list:
    dl.insertfirst(i)
dl.removelast()
string1=input("enter the string to be added to end of the linked list= ")
dl.insertlast(string1)
string2=input("enter the string to be added to the beginning of the list= ")
dl.insertfirst(string1)
dl.addafternode(dl.head.next.next,'hello')
dl.printlist()


