numbers = int(input())
for number in range(1,numbers+1):
    if numbers%number == 0:
        print(number, end=' ') 
