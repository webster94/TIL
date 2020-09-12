T = int(input())
for tc in range(1, T+1):
    a = input()
    b = input()
    
    letters = []
    for i in a:
        if i not in letters:
            letters.append(i)
            
    result = [0]*len(letters)
    
    for j in range(len(letters)):
        result[j] = b.count(letters[j])
    
    print('#{} {}'.format(tc, max(result)))
