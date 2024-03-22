#enqueue
#dequeue
#isempty
#rare
#Head
#isfull
#first element
queue=[]
def enqueue():
    if (len(queue)==n):
        return "The queue is full"
        
    else:
        element=int(input("enter an element:"))
        queue.append(element)
        return queue
def dequeue():
    if not queue:
        return "The queue is Empty"
    else:
        queue.pop(0)
        print(queue)
def isempty():
    if not queue:
        return "The queue is empty:"
    else:
        return "The queue is not empty"
def rare():
    if not queue:
        return "The queue is empty:"
    else:
        return queue[-1]
def head():
    if not queue:
        return "The queue is empty:"
    else:
        return queue[0]
def isfull():
    if len(queue)==n:
        return "The stack is full"
    else:
        return "The stack is not full"
def display():
    return queue
n=int(input("Enter length of a queue:"))
while (True):
    print("1.enqueue 2.dequeue 3.isempty 4.back 5.front 6.full 7.display 8.quit")
    choice=int(input("Enter choice:"))
    if (choice==1):
        print(enqueue())
    elif (choice==2):
        print(dequeue())
    elif (choice==3):
        print(isempty())
    elif (choice==4):
        print(rare())
    elif (choice==5):
        print(head())
    elif (choice==6):
        print(isfull())
    elif (choice==7):
        print(display())
    elif (choice==8):
        break
    else:
        print("Enter valid number to continue")
        
    
