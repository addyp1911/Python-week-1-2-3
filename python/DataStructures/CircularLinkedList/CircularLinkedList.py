import CircularLinkedListBL as cl:
c=cl.CircularLinkedList()
size=int(input("enter the size of the linked list= "))
for i in range(size):
    data=input("enter the user entered data= ")
    c.addfirst(data)
    c.addfirst(data)
    c.addlast(data)
    c.addfirst(data)
c.printlist()
c.removefirst()
c.removelast()
c.printlist()    