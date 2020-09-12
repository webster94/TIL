queue = [0] * 10

front = rear = -1

def enQueue(item):
    global rear
    if rear == len(queue)-1:
        print("가득참")
        return
    rear+=1
    queue[rear] = item

def deQueue():
    global front
    if front == rear:
        print("공백상태")
        return
    front += 1
    return queue[front]



