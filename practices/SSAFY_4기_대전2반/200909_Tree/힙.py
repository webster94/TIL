def heap_push(item):
    global heap_count
    heap_count += 1
    heap[heap_count] = item

    cur = heap_count
    parent = cur // 2

    # 루트가 아니고, if 부모노드값 > wktlrshemrkqt -> 스왑
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heap_pop():
    global heap_count
    item = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= heap_count:  # 오른쪽 자식 존재
        if heap[child] > heap[child + 1]:
            child = child + 1

    # 자식노드가 존재하고,  부모노드 > 자식노드 -> 스왑
    while child <= heap_count and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:  # 오른쪽 자식 존재
            if heap[child] > heap[child + 1]:
                child = child + 1
    return item

# 최소힙
heap_count = 0

temp = [7, 2, 5, 3, 4, 6]
N = len(temp)

heap = [0] * (N + 1)

for i in range(N):
    heap_push(temp[i])
print(heap)
for i in range(N):
    print(heap_pop())
