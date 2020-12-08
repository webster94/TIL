def moonwalk(index):
    if index == N:
        # print(arr[index] , end = ' ')
        print()
        return
    print(arr[index],end = ' ')
    moonwalk(index+1)

    print(arr[index], end=' ')


arr = input()
N = len(arr)
moonwalk(0)
arr[0]
