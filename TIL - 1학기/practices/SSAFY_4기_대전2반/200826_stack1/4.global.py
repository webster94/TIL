
def func():
    global ans
    # global top
    #
    # top += 1
    ans = 1
    memo[2] = 10
    # memo = [1,2,3,4,5]

top = -1
ans = 0
memo = [1,2,3,4]
func()

print(ans)
print(memo)

