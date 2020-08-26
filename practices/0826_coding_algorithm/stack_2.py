stack = []  # 빈스택을 하나 만들고
def push(item): # push는 어팬드하면 된다
    stack.append(item)

def pop(): # 비어있는 것을 확인해야한다.
    if len(stack) == 0 :
        print("Stack is Empty!")
        return
    else:
        return stack.pop()


push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())