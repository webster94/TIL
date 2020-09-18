# lambda 익명함수

def add(x, y):
    return x + y


add2 = lambda x, y: x + y

# print((lambda x, y: x + y)(3, 5))
# print(add(3, 5))
# print(add2(5, 5))
#  -1 -2 -3 -4

 #-기호를 붙이면 작았던 값이 커지는 효과 따라서 내림차순으로 정렬.
def f1(x):
    return -x[0]

ans = [[2, 3], [3, 4], [12, 4], [4, 5], [6, 8]]


num = sorted(ans, key = f1)

print(num)