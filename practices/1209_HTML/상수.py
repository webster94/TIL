A,B = input().split()
A = A[::-1]
B = B[::-1]
result = []
result.append(int(A))
result.append(int(B))
print(max(result))