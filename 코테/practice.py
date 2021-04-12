def Pactorial(Number):
    global result
    if Number < 2 :
        return 1
    result *=Number
    return Number * Pactorial(Number-1)
N = int(input())
result = 1
Pactorial(N)
print(result)
