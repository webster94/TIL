def Fibo(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return Fibo(n - 2) + Fibo(n-1)
N = int(input())
print(Fibo(N))
