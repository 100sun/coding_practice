import heapq  # min_heap

heap_items = [1, 3, 5, 7, 9]
min_heap, max_heap, li = [], [], []

for item in heap_items:
    heapq.heappush(min_heap, item)
    heapq.heappush(max_heap, (-item, item))  # y = -x
heapq.heappop(min_heap)  # root node of min_heap
heapq.heapify(li)  # list to heap
