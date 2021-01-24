def palindrome(char_list, N, M):
    success_list = []
    for i in range(N-M+1):
        if char_list[i:i+M] == char_list[i:i+M][::-1]:
            success_list.append(char_list[i:i+M])
    return success_list

T = int(input()) 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
     
    blanks = []
    for i in range(N):
        ABCs = list(",".join(input()).split(","))
        blanks.append(ABCs)
     
    word_list = []
    for k in range(N):
        A = palindrome(blanks[k], N, M)
        word_list.extend(A)
        
        
    for l in range(N):
        col_list = []
        for m in range(N):
            B = blanks[m][l]
            col_list += [B]
        C = palindrome(col_list, N, M)
        word_list.extend(C)
    
    for word in word_list:
        print("#{} {}".format(test_case, "".join(word)))
