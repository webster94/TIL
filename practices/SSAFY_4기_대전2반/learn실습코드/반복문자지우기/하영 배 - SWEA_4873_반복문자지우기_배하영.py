T = int(input())
for tc in range(1, T + 1):
    line = input()
    st = []
    for l in line:
        if len(st):
            if l == st[-1]:
                st.pop()
            else:
                st.append(l)
        else:
            st.append(l)
    print('#{} {}'.format(tc, len(st)))
