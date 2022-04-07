
class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	

	def __init__(self):
		self.head = None
  self.tail=None
      
  
        

	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		
		ptr1.next = self.head

		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = ptr1

		else:
			ptr1.next = ptr1 

		self.head = ptr1

	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print (temp.data, end=" ")
				temp = temp.next
				if (temp == self.head):
					break



cllist = CircularLinkedList()


while(True):
    print()
    print("Enter 1 for inertion")
    print("Enter 2 for display")
    print("Enter 3 for Exit")
    choice=input()
    if choice=='1':
        data=input()
        cllist.push(data)
    elif(choice=='2'):
        cllist.printList()    
    elif(choice=='3'):
        break    





