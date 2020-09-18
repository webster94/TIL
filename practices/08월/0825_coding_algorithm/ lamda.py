#lambda 익명함수
def add(x,y):
    return x,y

print((lambda x,y : x + y)(3,5))

add2 = lambda x , y : x+y

print(add(3,5))
print(add2(5,5))