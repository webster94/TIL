N = int(input())
tc = input()
result = ''
bin = {}
numbers = input().split()
for i in numbers:
    bin[i] = bin.get(i,0)+1

li = ['ZRO', "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for i in li:
    result += (i+' ') * bin[i]
print(result)