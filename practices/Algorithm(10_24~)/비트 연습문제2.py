
# 16진수 > 2진수(7개씩 끊어서) > 10진 수 변환
number16 = 0x01D06079861D79F99F
number2 = bin(number16)
for i in range(2,len(number2),7):
    print(int(number2[i:i+7],2) , end = ' ')

