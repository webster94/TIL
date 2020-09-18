num = int(input())
numbers = list(map(int,input().split()))
number_sort = sorted(numbers)
middle = number_sort[(len(numbers)//2)]
print(middle)
