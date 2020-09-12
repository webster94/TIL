# 전위순회
def preorder(n):
    pre_trav.append(bin_tree[n])
    if bin_tree[n * 2]:
        preorder(n * 2)
    if bin_tree[n * 2 + 1]:
        preorder(n * 2 + 1)

# 중위순회
def inorder(n):
    if bin_tree[n * 2]:
        inorder(n * 2)
    in_trav.append(bin_tree[n])
    if bin_tree[n * 2 + 1]:
        inorder(n * 2 + 1)

#후위순회
def postorder(n):
    if bin_tree[n * 2]:
        postorder(n * 2)
    if bin_tree[n * 2 + 1]:
        postorder(n * 2 + 1)
    post_trav.append(bin_tree[n])

pre_trav = []
in_trav = []
post_trav = []

E = 12
nums = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
bin_tree = [0] * (E ** 2)

for n in range(E):
    parent = nums[n * 2]
    child = nums[n * 2 + 1]

    # 부모 찾기
    if parent not in bin_tree:
        i = 0
    else:
        i = bin_tree.index(parent)

    # 자식 추가
    # 트리가 빈 경우
    if i == 0:
        bin_tree[i + 1], bin_tree[i + 2] = parent, child

    # 하나라도 있는 경우
    else:
        if bin_tree[i * 2] == 0:
            bin_tree[i * 2] = child
        else:
            bin_tree[i * 2 + 1] = child

preorder(1)
inorder(1)
postorder(1)

print('전위순회:', end =" ")
for i in pre_trav:
    print(i, end=" ")
print('\n중위순회:', end=" ")
for i in in_trav:
    print(i, end=" ")
print('\n후위순회:', end =" ")
for i in post_trav:
    print(i, end=" ")