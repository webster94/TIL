sentence = 'algorithm'
result = ''
print(sentence)
sentence=list(sentence)
print(sentence)
sentence[0],sentence[8] = sentence[8],sentence[0]
sentence[1],sentence[7] = sentence[7],sentence[1]
sentence[2],sentence[6] = sentence[6],sentence[2]
sentence[3],sentence[5] = sentence[5],sentence[3]
sentence=''.join(sentence)
print(sentence)

def str_rev(str):
    arr = list(str)
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    str = ''.join(arr)
    return str
    # ----------------
str = "algorithm"
str1 = str_rev(str)
print(str1)

s = "algorithm"
s = s[::-1]
print(s)

