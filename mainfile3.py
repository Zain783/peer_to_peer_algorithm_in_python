


class Node:    

  def __init__(self,data,id1):

    self.id = id1;    

    self.data = data;    

    self.next = None;

    self.prev = None;

    self.firstlink = None;

    self.secondlink = None;

    self.thirdlink = None;    

    self.fourthlink = None; 

class CreateList:
  TotalNodeCount=0  
  

  def __init__(self):    

    self.head = Node(None,0);    

    self.tail = Node(None,0);    

    self.head.next = self.tail;    

    self.tail.next = self.head;    
         
  

  def add(self,data,id):

    CreateList.TotalNodeCount=CreateList.TotalNodeCount+1

    newNode = Node(data,id);    


    if self.head.data is None:    

      self.head = newNode;    

      self.tail = newNode;    

      newNode.next = self.head;

      newNode.prev = self.tail;

      # countNode=countNode+1    

    else:    

      #tail will point to new node.    

      self.tail.next = newNode;

      newNode.prev=self.tail;    

      #New node will become new tail.    

      self.tail = newNode;    

      #Since, it is circular linked list tail will point to head.  

      self.head.prev = self.tail;  

      self.tail.next = self.head;

      # countNode=countNode+1
          
     

  #Displays all the nodes in the list    

  def displayClockwise(self):    

    current = self.head;    

    if self.head is None:    

      print("List is empty");    

      return;    

    else:

        print("node count is ",CreateList.TotalNodeCount)
        print()    

        print("Nodes of the circular linked list: ");    

        #Prints each node by incrementing pointer. 

        print("|",current.id,end=","),   

        print(current.data,end=" |->"),

        while(current.next != self.head):    

            current = current.next;

            print("|",current.id,end=","),    

            print(current.data,end=" |->"),    

  def displayAntiClockwise(self):    

    current = self.tail;    

    if self.head is None:    

      print("List is empty");    

      return;    

    else:    

        print("Nodes of the circular linked list: ");

        print("node count is ",CreateList.TotalNodeCount)
        print()   

        #Prints each node by incrementing pointer. 

        print("|",current.id,end=","),   

        print(current.data,end=" |->"),

        while(current.prev != self.head.prev):    

            current = current.prev;

            print("|",current.id,end=","),    

            print(current.data,end=" |->"),    

  def joinNode(self):

    current = self.head;    

    if self.head is None:    

      print("List is empty");    

      return;    

    else:
        id=input("Enter node number or id to search:")
        id=int(id)
        joinCount=0;
        if(current.id==id):
              print("|",current.id,end=","),   
              print(current.data,end=" |->"),
              print("node is founded...")
              # joinNodeNumberat0=current.id*2^joinCount
              # if(CreateList.TotalNodeCount>=joinNodeNumberat0):
              #     while(joinCount<=3):
              #         # current = self.head;
              #     # FORMULA FOR NODE JOIN
              #      joinNodeNumber=current.id*2^joinCount
              #      if(CreateList.TotalNodeCount>=joinNodeNumber):
              #           tempcurrent=current;
              #           while(current.next != self.head):
              #                 if(joinCount==0):
              #                   if(current.id==joinNodeNumber):
              #                     tempcurrent.firstlink=current.prev
              #                 elif(joinCount==1):
              #                   if(current.id==joinNodeNumber):
              #                     tempcurrent.secondlink=current.prev    
              #                 elif(joinCount==2):
              #                   if(current.id==joinNodeNumber):
              #                     tempcurrent.thirdlink=current.prev    
              #                 elif(joinCount==3):
              #                   if(current.id==joinNodeNumber):
              #                     tempcurrent.fourthlink=current.prev       
              #                 current = current.next;
              #      joinCount=joinCount+1           
              # joinCount=0      
                    # nextnode=current.next
                    # current.firstlink=nextnode.prev
        elif(current.id!=id):     
          while(current.next != self.head):
            if(current.id==id):    
              print("|",current.id,end=","),    
              print(current.data,end=" |->"),
              print("Node is founded...")
          #     while(joinCount<=3):
          #     # current = self.head;
          #     # FORMULA FOR NODE JOIN
          #      joinNodeNumber=current.id*2^joinCount
          #      if(CreateList.TotalNodeCount>=joinNodeNumber):
          #           tempcurrent=current;
          #           while(current.next != self.head):
          #                 if(joinCount==0):
          #                   if(current.id==joinNodeNumber):
          #                     tempcurrent.firstlink=current.prev
          #                 elif(joinCount==1):
          #                   if(current.id==joinNodeNumber):
          #                     tempcurrent.secondlink=current.prev    
          #                 elif(joinCount==2):
          #                   if(current.id==joinNodeNumber):
          #                     tempcurrent.thirdlink=current.prev    
          #                 elif(joinCount==3):
          #                   if(current.id==joinNodeNumber):
          #                     tempcurrent.fourthlink=current.prev       
          #                 current = current.next;
          #      joinCount=joinCount+1           
            current = current.next;                    
                 
              
              # print(current.id)
              # break

        else:
              print("Node is not founded....")
              
             
            

# class CircularLinkedList:    
nodeid=0
cl = CreateList() 

while(True):
    
    # NodeCount
    print()

    print("Enter 1 for inertion")

    print("Enter 2 for display")

    print("Enter 3 for Exit")

    choice=input()

    if choice=='1':

        # num_id =input("Enter id")

        data=input("Enter data")

        # id=int(num_id)
        

        cl.add(data,nodeid);
        nodeid=nodeid+1

    elif(choice=='2'):

        cl.displayClockwise();
        cl.joinNode();
        # print()

        # cl.displayAntiClockwise()    

    elif(choice=='3'):

        break    


  

