import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    sens1 = input()
    sens2 = input()
    nums1 = len(sens1)
    nums2 = len(sens2)
    result = 0
    for num2 in range(nums2-nums1+1):
        if sens2[num2] == sens1[0]:
            for i in range(nums1):
                if sens1[i] != sens2[num2+i]:
                    result = 0
                    break
                else:
                    result = 1
            if result:
                break
    print("#{} {}".format(tc, result))

