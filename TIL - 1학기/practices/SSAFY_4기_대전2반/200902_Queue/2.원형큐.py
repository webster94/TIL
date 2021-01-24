# 모듈로 연산
queue = [0] * 4

front = rear = 0


def enQueue(item):
    global rear
    if (rear + 1) % len(queue) == front:
        print("가득참")
        return
    rear = (rear + 1) % len(queue)
    queue[rear] = item


def deQueue():
    global front
    if front == rear:
        print("공백상태")
        return
    front = (front+1)%len(queue)
    return queue[front]

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)

print(queue)

print(deQueue())
print(deQueue())
print(deQueue())
enQueue(6)
enQueue(7)
print(queue)
