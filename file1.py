class Node:
     
    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None
class ringofnode:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion(self):
        data=input("Enter data:");
        temp=Node(data)
        if(head==None):
            
            head=temp
            tail=temp
            tail.next=head
        elif(head!=None):
            tail.next=temp
            tail=temp
            tail.next=head
    # def display(self):
    #     ptr=head
    #     if(ptr==None):
    #         print("no node is exists yet")
    #     else:
    #         print(ptr.data)
    #         ptr=ptr.next    
    #         while(ptr!=head):
    #             print(ptr.data,end="->")
    #             ptr=ptr.next
                    
                

 


# l1.display()


