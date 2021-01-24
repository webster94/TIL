def delete_repeat(s):
    for char in s:
        if char_list = [] or char_list[-1] != char:
            char_list.append(char)
        elif char_list != [] and char_list[-1] == char:
            char_list.pop()
    return len(char_list)
        

T = int(input())
for tc in range(1, T+1):
    s = list(input())
    char_list = []
    
    print("#{} {}".format(tc, delete_repeat(s)))