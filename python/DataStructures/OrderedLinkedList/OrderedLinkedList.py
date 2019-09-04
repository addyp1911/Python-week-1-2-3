
import OrderedLinkedListBL as ol

ll=ol.OrderedLinkedList()
file1=open(r"/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()
for i in file_content:
<<<<<<< HEAD
    ll.addfirst(i)
ll.printlist()
=======
    ll.addFirst(i)
    ll.printList()
>>>>>>> 8fe8be723c476187e1b13f5f22e9069af8611f62
print("the sorted list is ",ll.sort())






