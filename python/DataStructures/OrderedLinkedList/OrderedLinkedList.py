


import OrderedLinkedListBL as ol

ll=ol.LinkedList()
file1=open(r"/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()
list1=[]
for i in file_content:
    list1.append(int(i))
    ll.addFirst(i)
    ll.printList()
print("the sorted list is ",ll.sort(list1))






