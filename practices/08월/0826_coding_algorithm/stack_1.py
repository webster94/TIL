# C style
def push(item):
    global top
    if top > 100 -1: #(0~99까지 인덱스가 있으니까)
        return
    else:
        top += 1
        stack[top] = item

def pop():  # isEmpty 를 반드시 써야한다. 확인체크필수!
    global top
    if top == -1:
        print("Stack is Empty!!!")
        return
    else:
        result = stack[top]
        top += -1
        return result

stack = [0]* 100 # 배열은 고정이다. append 안 쓰겠다 인덱스를 활용하겠다.
top = -1 #(항상 -1로 초기화해야한다)
# top// stack
# top 은 값형  읽기만 된다! 값을 바꾸기 위해선 global을 작성해줘야한다.
# stack은 참조형 읽고 쓰기가 다 된다.
push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())