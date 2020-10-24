
Binary = '0000000111100000011000000111100110000110000111100111100111111001100111'
print (len((list(Binary))))
for i in range(0,len(list(Binary))+1,7):
    y = Binary[i:i+7]
    base = 10
    answer = 0
    for idx,j in enumerate(y[::-1]):
        answer += int(j) * (base **idx)
    print(int(str(y),base))