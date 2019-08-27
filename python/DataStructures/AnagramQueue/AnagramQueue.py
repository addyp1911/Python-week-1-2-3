# Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Queue using
# the Linked List and Print the Anagrams from the Queue. Note no Collection Library
# can be used.

import AnagramQueueBL as aq

size=int(input("enter the size of the queue= "))
q=aq.Queue()
q.add(size)
q.printlist()