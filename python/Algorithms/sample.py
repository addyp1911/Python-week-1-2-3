
 
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None 


# Linked List class contains a Node object 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None


	# Functio to insert a new node at the beginning 
	def push(self, new_data): 

		# 1 & 2: Allocate the Node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 3. Make next of new Node as head 
		new_node.next = self.head 

		# 4. Move the head to point to new Node 
		self.head = new_node 


	def insertAfter(self, prev_node, new_data): 

		

		# 2. create new node & 
		#	 Put in the data 
		new_node = Node(new_data) 

		# 4. Make next of new Node as next of prev_node 
		new_node.next = prev_node.next

		# 5. make next of prev_node as new_node 
		prev_node.next = new_node 


	# This function is defined in Linked List class 
	# Appends a new node at the end. This method is 
	# defined inside LinkedList class shown above */ 
	def append(self, new_data): 

		# 1. Create a new node 
		# 2. Put in the data 
		# 3. Set next as None 
		new_node = Node(new_data) 

		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
			self.head = new_node 
			return

		# 5. Else traverse till the last node 
		last = self.head 
		while (last.next): 
			last = last.next

		# 6. Change the next of last node 
		last.next = new_node 


	# Utility function to print the linked list 
	def printList(self): 
		temp = self.head 
		while (temp): 
			print (temp.data) 
			temp = temp.next




if __name__=='__main__': 

	llist = LinkedList() 


	llist.append(6) 


	llist.push(7); 

	llist.push(1); 

	llist.append(4) 

	llist.insertAfter(llist.head.next, 8) 

	llist.printList() 

    