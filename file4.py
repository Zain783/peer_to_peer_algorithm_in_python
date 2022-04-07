class Node:
      def __init__(self, value = None):
            self.value = value
            self.next = None
            self.prev = None

#Create a circular doubly linked list class to initialize head and tail references
class CDoublyLinkedList:
      def __init__(self):
            self.head = None
            self.tail = None

       #Function to create Circular Doubly Linked List
      def createCDLL(self, value):
              new_node = Node(value)
              new_node.next = None
              new_node.prev = None
              self.head = new_node
              self.tail = new_node
              print("The circular doubly linked list has been created.")
      def printForwardList(self):
            if self.head == None:
             print("The linked list does not exist.")
            else:
                temp_node = self.head
                while True:
                    print(temp_node.value)
                    if temp_node == self.tail:
                        break
                    temp_node = temp_node.next
      


circulardoublyLL = CDoublyLinkedList()
circulardoublyLL.createCDLL(5)
circulardoublyLL.createCDLL(51)
circulardoublyLL.createCDLL(53)
circulardoublyLL.printForwardList()
