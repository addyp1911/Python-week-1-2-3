# UnOrdered List
# a. Desc -> Read the Text from a file, split it into words and arrange it as Linked List.
# Take a user input to search a Word in the List. If the Word is not found then add it
# to the list, and if it found then remove the word from the List. In the end save the
# list into a file
# b. I/P -> Read from file the list of Words and take user input to search a Text
# c. Logic -> Create a Unordered Linked List. The Basic Building Block is the Node
# Object. Each node object must hold at least two pieces of information. One ref to
# the data field and second the ref to the next node object.
# d. O/P -> The List of Words to a File.


import UnorderedLinkedListBL as ol

ll=ol.LinkedList()
file1=open(r"/home/admin1/Desktop/sample.txt",'r')
file_content=file1.read().split()
list1=[]
for i in file_content:
    list1.append(int(i))
    ll.addFirst(i)
    ll.printList()
print("the sorted list is ",ll.sort(list1))






