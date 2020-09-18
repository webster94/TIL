def fibo2(n):
    if n >= 2 and len(memo) <= n:
         # 리스트의 길이 # momo는 참조형이라 R,W가 다 된다.
        # 이미 가지고 있다는 뜻이다.
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0,1]
ans = 0
print(fibo2(7))