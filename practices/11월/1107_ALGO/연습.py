import heapq

heap = []
heapq.heappush(heap,5)
heapq.heappush(heap,4)
heapq.heappush(heap,7)
heapq.heappush(heap,1)
heapq.heappush(heap,3)
print(heap)
for i in range(len(heap)):
    print(heapq.heappop(heap))
