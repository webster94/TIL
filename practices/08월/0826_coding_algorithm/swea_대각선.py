li = [['+'] * 5 for _ in range(5)]
string = []
for i in range(5):
    for j in range(5):
        if i == j:
            li[i][j] = "#"
for i in range(5):
    for j in range(5):
        string.append(li[i][j])
    string.append('\n')
string =''.join(string)
print(string)

