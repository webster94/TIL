# zip 같은 열끼리 묶어서 표현을 해준다.
#열의 갯수가 안맞으면 맞는것 까지만 묶어줌
test1 = [1,2,3,4]
test2 = [5,6,7]

test3 = list(zip(test1, test2))

print(test3)

#이차원리스트도 가능
nums = [[1,2,3],[1,2,3]]

#모든 요소를 넣어줘도 좋고
nums2 = list(zip(nums[0],nums[1]))
#언팩킹을 하여 한번에 처리도 가능함.
nums3 = list(zip(*nums))
print(nums2)
print(nums3)

tmp = [1,2,3,4]

print(tmp)
print(*tmp)
print(list(zip(tmp)))